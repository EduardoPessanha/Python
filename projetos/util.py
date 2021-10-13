#!/usr/bin/env python3
# -*-coding:utf-8-*-
from sqlite3.dbapi2 import OperationalError
from tkinter import Tk, messagebox
from tkinter.ttk import Style
from sqlite3 import Error, connect
from os import path


class Estilo():
    def __init__(self, tema='classic') -> None:
        self.tema = tema

    def estilo(self, tema='classic'):
        """:param tema: define um tema -> 'clam', 'alt', 'default', 'classic'(padrão)
        """
        self.style = Style()
        self.style.theme_use(self.tema)
        return tema


class Conecta():
    def __init__(self, tema='classic') -> None:
        """
        param estilo: define um tema padrão -> 'clam', 'alt', 'default'ou  'classic'.
        """
        self.tema = tema
        Estilo().estilo()

    def condb(self, arq: str):
        """
        Estabelece uma conexão com um Banco de Dados.
        :param arq: nome do Banco de Dados.

        """
        dirdb = path.dirname((__file__))
        nomedb = f'{dirdb}/{arq}.db'
        try:
            # _Verifica se existe o banco de dados:
            if not path.isfile(nomedb):
                resp = messagebox.askyesno(
                    "Atenção", f"O banco de dados {arq}.db, não Existe!!!. Deseja cria-lo?")
                conexao = False
            else:
                resp = True
            if resp:
                # *O comando connect serve para conectar ou criar um Banco de Dados, caso ele não exista.
                conexao = connect(nomedb)
            else:
                return conexao
        except Error as err:
            messagebox.showerror(("Atenção ERRO: ", err))
            return
        return conexao


class Criadb():
    """
    Cria uma tabela em um Banco de dados, de acordo com as informações passadas
    pelo parâmetro 'cmdsql: ....str'
    :param arqdb: Nome do banco de dados.
    :param cmdsql: comandos SQL contendo as informações
    necessárias para a criação da tabela do banco de dados."""

    def __init__(self, arqdb: str) -> None:
        self.arqdb = arqdb
        
    def dml(self, cmdsql ):
        try:
            # Estabelecer conexão com o banco de dados:
            conn = Conecta().condb(self.arqdb)
            if conn:    # *Conexão estabelecida com sucesso!
                cursor = conn.cursor()
                cursor.execute(cmdsql)
                conn.commit()
            else:       # **Não foi estabelecida a conexão!
                return          # _Retorna 'None'
        except Error as err:
            if OperationalError('table tb_contato already exists'): # A tabela já existe!
                return conn     # _Retorna a conexão.
            print(f'\nOcorreu um ERRO: {err}\n')
        return conn             # _Retorna a conexão.


def main():
    tab = """
        CREATE TABLE tb_contato(
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(30),
                fone VARCHAR(14),
                email VARCHAR(30),
                endereco VARCHAR(30),
                cidade VARCHAR(30),
                uf VARCHAR(2),
                obs VARCHAR(500)
                );
        """
    arquivo = Criadb('Teste')
    print(arquivo)
    print(type(arquivo))
    a = arquivo.dml(tab)
    print(a)
    print(arquivo)
    print(f'\n{arquivo.arqdb}.db\n')

if __name__ == '__main__':
    main()
