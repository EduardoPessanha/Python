#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from datetime import date
import sqlite3
from sqlite3 import connect
from os import path


class Conecta():

    def __init__(self, arqdb: str):
        """
        Faz a conexão com um banco de dados

        Args:
            arqdb (str): nome do arquivo do banco de dados
        """
        try:
            self.arqdb = arqdb
            # Definindo o nome e caminho do banco de dados
            self.dir_banco_dados = path.dirname((__file__))
            self.nome_banco_dados = f'{self.dir_banco_dados}/{self.arqdb}.db'
            # Conectando ...
            self.conexao = connect(self.nome_banco_dados)
            self.cursor = self.conexao.cursor()
            return
        except sqlite3.Error:
            print('Erro ao abrir o banco de dados.')
            return

    def fecha_conexao(self):
        """
        Fecha a conexao do banco de dados se estiver aberta.
        """
        if self.conexao:
            self.conexao.close()
            print('Conexão encerrada!')

    def commit_bd(self):
        """
        Grava as alterações no banco de dados.
        """
        if self.conexao:
            self.conexao.commit()


class Banco_Dados():

    def __init__(self, nome_bd) -> None:
        self.b_dados = Conecta(nome_bd)
        self.tb_nome = nome_bd

    def abre_sql(self, nomesql):
        """
        Abre um arquivo que contém instruções/comandos SQL
        
        Args: nomesql (str): nome do arquivo que contém as instruções SQL
        Returns: str
        """
        self.cmdsql = nomesql
        # * Lendo o arquivo '.sql', que contem as instruções sql
        # * para a criação da tabela e salvando na variável 'cmdsql':
        with open(self.cmdsql, 'rt') as f:  # > 'rt' abre o arquivo para leitura ('r'), no modo texto ('t')
            instrucao_sql = f.read()
            instrucao_sql = instrucao_sql.replace(
                'nome_tabela', f't_{(self.tb_nome).lower()}')
        f.close()
        return instrucao_sql

    def criar_tabela(self):
        """ 
        Cria a tabela do banco de dados
        """
        self.cmdsql = self.abre_sql('tabela.sql')
        self.dml()

    def dml(self):
        """
        Criar, atualizar e apagar registros do banco de dados.
        """
        try:
            if self.b_dados.conexao:
                self.b_dados.cursor.executescript(self.cmdsql)
                self.b_dados.commit_bd()
                # self.b_dados.fecha_conexao()
                return
        except sqlite3.Error:
            if sqlite3.OperationalError('table tb_contato already exists'):
                print(
                    f'Aviso: A tabela \"t_{self.tb_nome.lower()}\" já existe ...')
                return

    def inserir_registro(self, lista: list):
        self.lista = lista
        self.cmdsql = self.abre_sql('insere.sql')
        try:
            if self.b_dados.conexao:
                self.b_dados.cursor.executemany(self.cmdsql, self.lista)
                self.b_dados.commit_bd()
        except sqlite3.Error:
            print('Atenção correu um ERRO....')
            return

    def listar_registro(self):
        self.cmdsql = self.abre_sql('exibe.sql')
        self.reg = self.b_dados.cursor.execute(self.cmdsql)
        print(f'{"ID":^4} {"Data":^12} {"Tipo":^8} {"Descrição":^17} {"Valor":^13} {"Saldo":^15} {"Obs":^18}')
        print('='*95)
        for r in self.reg:
            print(
                f'{r[0]:^4} {r[1]:^12} {r[2]:^8} {r[3]:<17} R${r[4]:>11.2f} R${r[5]:>11.2f} {r[6]:<26}')

    def editar_registro(self):
        ...

    def atualizar_registro(self):
        ...

    def apagar_registro(self):
        ...


if __name__ == '__main__':
    banco = Banco_Dados('Novo')
    # print(f'banco: {banco.tb_nome}.db')
    # print(type(banco))
    tabela = banco.criar_tabela()
    # print(type(tabela))
    # print(tabela)
    print('\n\n')
    # print(dir(Conecta))
    # print(dir(Banco_Dados))

    data = str(date.today()).replace('-', '/')
    # print(data)
    # v_reg = [(data, 'E', 'Deposito', 10000, 10000, 'Deposito inicial'),
    #          (data, 'S', 'Despesa', 270.58, 10000, 'Despesas de mercado'),
    #          (data, 'S', 'Despesa', 150.37, 10000, 'Outras despesas de mercado')]
    # banco.inserir_registro(v_reg)
    banco.listar_registro()
    banco.b_dados.fecha_conexao()
