#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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
            return None
            # self.cursor.execute('SELECT SQLITE_VERSION()')
            # self.data = self.cursor.fetchone()
            # # imprimindo a versão do SQLite
            # print(f"SQLite version: {self.data}")

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

    def criar_tabela(self):
        """ 
        Cria a tabela do banco de dados
        """
        # * Lendo o arquivo 'caixa_tabela.sql', que contem as instruções sql 
        # * para a criação da tabela e salvando na variável 'cmdsql':
        cmdsql = 'caixa_tabela.sql'
        with open(cmdsql, 'rt') as f:
            instrucao_sql = f.read()
        self.cmdsql = instrucao_sql
        self.dml()

    def dml(self):
        """
        Criar, atualizar e apagar registros do banco de dados.
        """
        try:
            if self.b_dados.conexao:
                self.b_dados.cursor.executescript(self.cmdsql)
                self.b_dados.commit_bd()
                self.b_dados.fecha_conexao()
        except sqlite3.Error:
            if sqlite3.OperationalError('table tb_contato already exists'):
                print(f'Aviso: A tabela {self.tb_nome} já existe ...')
                return


if __name__ == '__main__':
    banco = Banco_Dados('Teste').criar_tabela()
    # print(type(banco))
    # print(f'banco: {banco.tb_nome}.db')
    print(dir(Conecta))
