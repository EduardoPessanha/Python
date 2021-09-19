# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, messagebox
from sqlite3 import Error, connect
import os


def agenda():
    """
    ####    Estabelece a conexão com o banco de dados Agenda.db
    """
    dirdb = os.path.dirname(__file__)
    nomedb = dirdb + '/Agenda.db'
    con = connect(nomedb)
    return con


def limpatv(par):
    """
    ####    Função para limpar a tela da TreeView antes de mostrar os dados

        :param par: informa o nome da TreeView
    """
    treev = par
    treev.delete(*treev.get_children())
    """
    * OU:
    for i in treev.get_children():
        treev.delete(i)
    """


def tvw(master):
    """
        Gera a Treeview que exibe os registros da tabela tb_contatos
        do banco de dados Agenda.db

        :param master: objeto pai da Treeview
    """
    tela = master
    global treev
    #  _Treeview:
    # *- ****** Definindo as colunas ******
    colunas = ('id', 'nome', 'telefone', 'e-mail',
               'endereco', 'cidade', 'estado', 'observacao')
    treev = ttk.Treeview(tela, columns=colunas,
                         show='headings', padding=(1, 1))

    # *- ****** Definindo os cabeçalhos das colunas ******
    treev.heading('id', text='ID')
    treev.heading('nome', text='Nome')
    treev.heading('telefone', text='Telefone')
    treev.heading('e-mail', text='Email')
    treev.heading('endereco', text='Endereço')
    treev.heading('cidade', text='Cidade')
    treev.heading('estado', text='UF')
    treev.heading('observacao', text='Nota')

    # *- Adicionando uma scrollbar:
    scrollbarv = ttk.Scrollbar(tela, orient=[VERTICAL], command=treev.yview)
    scrollbarh = ttk.Scrollbar(
        tela, orient=[HORIZONTAL], command=treev.xview)
    treev.configure(yscroll=scrollbarv.set)
    treev.configure(xscroll=scrollbarh.set)

    # *- ***** Definindo o tamanho das colunas *****
    treev.column('id', width=35, minwidth=10, stretch=True, anchor=CENTER)
    treev.column('nome', width=170, minwidth=0, stretch=True)
    treev.column('telefone', width=115, minwidth=0, stretch=True)
    treev.column('e-mail', width=150, minwidth=0, stretch=True)
    treev.column('endereco', width=200, minwidth=0, stretch=True)
    treev.column('cidade', width=100, minwidth=0, stretch=True)
    treev.column('estado', width=35, minwidth=0, stretch=True, anchor=CENTER)
    treev.column('observacao', width=235, minwidth=0, stretch=True)

    # *- ****** Posicionando o elemento Treeview: ******
    treev.grid(column=0, row=2, padx=True, pady=True)
    scrollbarv.grid(row=2, column=1, sticky='ns')
    scrollbarh.grid(row=3, column=0, sticky='ew')

    # *- ****** Exibe os dados da tabela tb_contatos na Treeview: ******
    exibir(treev)
    # <Control-Button-1> <<TreeviewSelect>>
    treev.bind('<<TreeviewSelect>>', item_selected)
    return


def lfr2(master):
    """
    ####   Gera os elementos que serão posicionados no tela da tela principal

        :param master: objeto pai da LabelFrame
    """
    global txtnome, txtfone, txtmail, txtend, txtcid, txtuf, txtobs, lf2
    global btninser, btnedita, btnexclui

    lf2 = master
    # teste = StringVar(tela, 'isto é um teste')
    # _ Elementos label e texto (Entry):

    # _ Elemento label:

    lblnome = Label(lf2, text='Nome: ', width=8, anchor='w')  # _ , bg='#0ff'
    lblfone = Label(lf2, text='Telefone: ', width=8, anchor='w')
    lblmail = Label(lf2, text='E-mail: ', width=8, anchor='w')
    lblend = Label(lf2, text='Endereço: ', width=8, anchor='w')
    lblcid = Label(lf2, text='Cidade: ', width=8, anchor='w')
    lbluf = Label(lf2, text='UF: ', width=8, anchor='w')
    lblobs = Label(lf2, text='Nota: ', width=4, anchor='w')

    # _ Elemento texto (Entry):

    txtnome = Entry(lf2, width=25, font=(
        'Ebrima', 12), bd=1, justify='left')    # coluna 1   , textvariable=teste
    txtfone = Entry(lf2, width=15, font=(
        'Ebrima', 12), bd=1, justify='left')
    txtmail = Entry(lf2, width=25, font=(
        'Ebrima', 12), bd=1, justify='left')
    txtend = Entry(lf2, width=30, font=(
        'Ebrima', 12), bd=1, justify='left')    # coluna 3
    txtcid = Entry(lf2, width=25, font=(
        'Ebrima', 12), bd=1, justify='left')
    txtuf = Entry(lf2, width=2, font=('Ebrima', 12), bd=1, justify='left')
    txtobs = Text(lf2, width=29, height=4, font=(
        'Ebrima', 12), bd=1)  # coluna 5

    reglist = [txtnome, txtfone, txtmail, txtend, txtcid, txtuf, txtobs]

    # _ Elemento botão do LabelFrame:

    btninser = Button(lf2, text='Inserir', width=10, bg='#b8b1e0',
                      font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: inserir(reglist))
    btnedita = Button(lf2, text='Editar', width=10, bg='#b8b1e0',
                      font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: dml('editar'), state='disabled')
    btnexclui = Button(lf2, text='Excluir', width=10, bg='#b8b1e0',
                       font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: dml('excluir'), state='disabled')
    btnreset = Button(lf2, text='Atualizar', width=10, bg='#b8b1e0',
                       font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=atualiza)

    # _ Posicionando os elementos dentro do LabelFrame:

    lblnome.grid(column=0, row=1)
    txtnome.grid(column=1, row=1, padx=5, pady=2, sticky='w')
    lblfone.grid(column=0, row=2)
    txtfone.grid(column=1, row=2, padx=5, pady=2, sticky='w')
    lblmail.grid(column=0, row=3)
    txtmail.grid(column=1, row=3, padx=5, pady=2, sticky='w')
    lblend.grid(column=2, row=1)
    txtend.grid(column=3, row=1, padx=5, pady=2, sticky='w')
    lblcid.grid(column=2, row=2)
    txtcid.grid(column=3, row=2, padx=5, pady=2, sticky='w')
    lbluf.grid(column=2, row=3)
    txtuf.grid(column=3, row=3, padx=5, pady=2, sticky='w')
    lblobs.grid(column=4, row=1)
    txtobs.grid(column=5, row=1, padx=5, pady=2, sticky='wn', rowspan=3)
    btninser.grid(column=1, row=4, pady=5)
    btnedita.grid(column=3, row=4, padx=2.5)
    btnexclui.grid(column=5, row=4, padx=5)
    btnreset.grid(column=3, row=5, padx=5, pady=10)
    return


def lfr3(master):
    """
    #### Gera os elementos que serão posicionados no tela da tela principal

        :param master: objeto pai da LabelFrame
    """
    lf3 = master

    # * Elementos label e texto (Entry) do LabelFrame frame3:
    # * Elemento label

    lblnome1 = Label(lf3, text='Nome: ', width=5, anchor='w')

    # -* Elemento texto (Entry) do LabelFrame frame3:

    txtnome1 = Entry(lf3, width=30, font=('Ebrima, 12'), justify='left')

    # -* Elemento botão do LabelFrame frame3:

    btnpesq = Button(lf3, text='Pesquisar', width=10, bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: pesquisa(treev, txtnome1))
    btntudo = Button(lf3, text='Mostrar Tudo', width=10, bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: exibir(treev))  # _ flat, groove, raised, ridge, solid, or sunken
    btnsair = Button(lf3, text='Sair', width=10, bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=sair)

    # -* Posicionando os elementos dentro do frame3:

    lblnome1.grid(column=0, row=0, padx=5)
    txtnome1.grid(column=1, row=0, padx=5, sticky='w')
    btnpesq.grid(column=2, row=0, padx=10, pady=10)
    btntudo.grid(column=3, row=0, padx=5, pady=10)
    btnsair.grid(column=6, row=0, padx=10, pady=10)

    return


def inserir(val: list):
    """
    #### Função para inserir um novo registro na tabela do banco de dados

        :param val: lista contendo os registro a serem inseridos na tabela tb_contatos do banco de dados Agenda.db
    """

    txtnome = val[0]
    txtfone = val[1]
    txtmail = val[2]
    txtend = val[3]
    txtcid = val[4]
    txtuf = val[5]
    txtobs = val[6]

    vcon = agenda()         # * Abre o banco de dados
    po = vcon.cursor()      # * Definindo o cursor para receber a conexão

    try:
        if txtnome.get() == '' or txtfone.get() == '' or txtmail.get() == '':
            # ** O formulário está em branco
            messagebox.showerror(
                'ATENÇÃO ERRO', 'Não foram informados os valores!')
        else:
            # > 3- Ler os dados inseridos do formulário
            reg = f"""INSERT INTO tb_contatos 
                (t_nome, t_fone, t_email, t_endereco, t_cidade, t_uf, t_obs)
                VALUES("{txtnome.get()}", "{txtfone.get()}", "{txtmail.get()}", 
                "{txtend.get()}", "{txtcid.get()}", "{txtuf.get().upper()}", 
                "{txtobs.get(1.0, END)}")
            """
        # > 4- Inserir os dados do formulário na tabela do banco de dados e fazer o commit (atualizar o banco de dados)
            po.execute(reg)
            vcon.commit()
            messagebox.showinfo('AVISO', 'Registro inserido com sucesso!')
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)
    finally:
        # > 5- Limpando os dados do formulário e fechando o banco de
        limpatxt()
        txtnome.focus()

        vcon.close()  # _ fecha a conexão
    return


def sair():
    """ 
    #### Encerra o aplicativo
    """
    os.system('clear')
    exit()
    return


def pesquisa(inf, txt):
    """
    ####    Executa uma pesquisa no banco de dados por um nome e mostra na TreeView

        :param inf: informa o nome da Treeview
        :param txt: informa o nome para a pesquisa
    """
    tv = inf
    txtnome1 = txt

    # > Conectando o banco de dados:
    vcon = agenda()
    po = vcon.cursor()
    vnome = txtnome1.get()
    try:
        # _ Conulta por nome:
        if vnome == '':
            messagebox.showerror(
                'ATENÇÃO ERRO', 'Informe um nome para pesquisar')
        else:
            vsql = 'SELECT * FROM tb_contatos WHERE t_nome LIKE "%'+vnome+'%"'
            po.execute(vsql)
            vreg = po.fetchall()
            # - Limpar os dados da TreeView:
            limpatv(inf)
            for i in vreg:
                reg = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                tv.insert('', 'end', values=reg)
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)
    finally:
        # > Limpando a caixa de texto e fechando o banco de dados:
        txtnome1.delete(0, END)
        vcon.close()  # _ fecha a conexão
    return


def exibir(inf):
    """
    #### Abre um banco de dados Agenda.db, seleciona os registros da tabela tb_contatos e os exibe na tela da TreeView

        :param inf: informa o nome da Treeview
    """
    vcon = agenda()  # - Abrindo o banco de dados

    # - Limpando a tela da TreeView antes de mostrar os dados:
    limpatv(inf)

    try:
        # *- ****** Inserindo os dados na Treeview: ******
        # * Os dados da Treeview serão os registro da tabela tb_contatos do banco de dados Agenda.db

        # *- Abrindo o banco de dados:
        vcon = agenda()
        c = vcon.cursor()  # _ criar um cursor para receber a conexão
        # * execução da consulta (query) pelo cursor:
        c.execute('select * from tb_contatos')
        res = c.fetchall()  # _ criar uma lista contendo todos os registros da tabela tb_contatos
        vcon.close()  # _ fechar a conexão

    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)

    finally:
        # - Inserindo (exibir) os registros na Treeview:
        for i in res:
            treev.insert('', 'end', values=[i[0], i[1],
                                            i[2], i[3], i[4], i[5], i[6], i[7]])
    return


def dml(tipo: str):     # query = consulta
    """
        #### Abre um banco de dados e realiza alterações nos seus registros.

        :param tipo: informa o tipo de consulta, se excluir ou atualizar
    """
    vID = record[0]
    try:
        res = messagebox.askquestion('CONFIRMAR', 'Deseja continuar?')
        vcon = agenda()   # abrir a conexão
        if tipo == 'excluir':   #_ Excluir o registro
            if res == 'yes':
                consulta = f'DELETE FROM tb_contatos WHERE n_id = {vID}'
                c = vcon.cursor()    # criar um cursor para receber a conexão
                c.execute(consulta)    # execução da consulta (query) pelo cursor
        elif tipo == 'editar':  #_ Editar o registro
            nome = txtnome.get()
            fone = txtfone.get()
            mail = txtmail.get()
            end = txtend.get()
            cid = txtcid.get()
            uf = txtuf.get()
            obs = txtobs.get(1.0, END)
            if res == 'yes':
                consulta = f'UPDATE tb_contatos SET t_nome = "{nome}", t_fone = "{fone}", t_email= "{mail}", t_endereco= "{end}", t_cidade= "{cid}", t_uf = "{uf}", t_obs = "{obs}" WHERE n_id = {vID}'
                c = vcon.cursor()    # criar um cursor para receber a conexão
                c.execute(consulta)    # execução da consulta (query) pelo cursor
    except Error as err:
        print(f'ATENÇÃO ERRO: {err}')
    finally:
        vcon.commit()   # confirmação dos dados que foram manipulados
        vcon.close()    # fechar a conexão
        atualiza()
        btninser.config(state='normal')
        btnedita.config(state='disabled')
        btnexclui.config(state='disabled')
        txtnome.focus()
    return


def atualiza():
    limpatxt()
    exibir(treev)
    return


def item_selected(evento):
    global vID, record

    for selected_item in treev.selection():

        btninser.config(state='disabled')
        btnedita.config(state='normal')
        btnexclui.config(state='normal')

        item = treev.item(selected_item)    # dictionary
        record = item['values']             # list

        limpatxt()
        vID = record[0]
        txtnome.insert(0, record[1])
        txtfone.insert(0, record[2])
        txtmail.insert(0, record[3])
        txtend.insert(0, record[4])
        txtcid.insert(0, record[5])
        txtuf.insert(0, record[6])
        txtobs.insert(END, record[7])
    return


def limpatxt():
    """
    #### Limpa os elementos Entry e Text do frame2
    """
    txtnome.delete(0, END)
    txtfone.delete(0, END)
    txtmail.delete(0, END)
    txtend.delete(0, END)
    txtcid.delete(0, END)
    txtuf.delete(0, END)
    txtobs.delete(1.0, END)
    return


def main():
    pass
    print("""
    # >                         EXCLUIR/ EDITAR
    # **Para Excluir e Editar verificar se poderemos usar a função dml(),
    # **com algumas adaptações para isso.
    # **Após excluir ou editar NÃO esquecer de limpar os campos da frame2.
    # - Passo 1: Selecionar qual registro deverá ser excluído/editado!
    # - Selecionando um registro:
    # O registro que for selecionado na Treeview será vinculando(bind) e inserido nos elementos Entry e text do frame2 -> FEITO
    # nos campos do contato da frame2, quando os botões Excluir e Editar forem habilitados o botão Inserir será desabilitado. -> FEITO
    # Os botões de Excluir e Editar deverão passar para a frame2 -> FEITO
    # Passo 2: Confirmar a exclusão/edição -> FEITO
    # Passo 3: Excluir/editar o registro -> FEITO
    # Passo 4: Limpar os elementos Entry e Text da frame2 -> FEITO
    # Passo 5: Desabilitar os botões Excluir e Editar e habilitar o botão Inserir -> FEITO
    # Passo 6: Atualizar a Treeview (treev) para mostrar as alterações realizadas -> FEITO
    """)
    return


if __name__ == '__main__':
    main()
