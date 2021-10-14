#!/usr/bin/env python3
# -*-coding:UTF-8-*-
"""

Protótipo de layout de interface gráfica para cadastro de contatos

"""
from tkinter import Button, Entry, Text, Frame, LabelFrame
from tkinter import PanedWindow, Label, mainloop, Tk, ttk, messagebox
from util import Conecta, Criadb
from sqlite3 import Error


# *Programando os comandos dos botões:
# >Botão Inserir:
def inserir():
    # _1. Ler os registros digitados no formulário lfr)formulário,
    v_nome = txt_nome.get()
    v_fone = txt_fone.get()
    v_mail = txt_mail.get()
    v_end = txt_end.get()
    v_cid = txt_cid.get()
    v_uf = txt_uf.get()
    v_obs = txt_obs.get(1.0, 'end')

    # _2. Confirmar que  pelo menos o campo nome foi preenchido.
    if v_nome == '':
        messagebox.showerror(
            'ATENÇÃO ERRO', 'Não foram informados os valores!')
        return      # **sair da rotina
    else:
        # _3. Formatando os novos registros:
        v_sql = f"""INSERT INTO tb_contato 
                        (Nome, Fone, Email, Endereco, Cidade, UF, Obs)
                        VALUES("{v_nome}", "{v_fone}", "{v_mail}", 
                        "{v_end}", "{v_cid}", "{v_uf.upper()}", 
                        "{v_obs}")
                    """
        # _Abrindo o banco de dados e iInserindo os novos registros:
        conexao = Criadb('Cadastro')
        con = conexao.dml(v_sql)

        # _4. limpar os campos do formulário, fechar a conexão e atualizar a Treeview:
        # **limpar os campos:
        limpatxt()
        # **Fechando o banco de dados:
        con.close()
        # **Atualizar a Treeview:
        reset()
    return


# >Botão Pesquisar:
def pesquisa(args):
    """
        Executa uma pesquisa no banco de dados por um nome e mostra na TreeView

        :param inf: informa o nome da Treeview
        :param txt: informa o nome para a pesquisa
    """
    v_nome = args
    try:
        v_nome = txt_nome1.get()
        # _ Conulta por nome:
        if v_nome == '':
            messagebox.showerror(
                'ATENÇÃO ERRO', 'Informe um nome para pesquisar')
            return
        else:
            v_sql = 'SELECT * FROM tb_contato WHERE Nome LIKE "%'+v_nome+'%"'
            # > Conectando o banco de dados:
            con = Conecta().condb('Cadastro')
            cursor = con.cursor()
            cursor.execute(v_sql)
            v_reg = cursor.fetchall()
            # - Limpar os dados da TreeView:
            limpatv(treev)
            # - Inserindo os dados editados:
            for i in v_reg:
                reg = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                treev.insert('', 'end', values=reg)
            # > Limpando a caixa de texto e fechando o banco de dados:
            txt_nome1.delete(0, 'end')
            treev.focus_set()
            con.close()  # _ fecha a conexão
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)
    return


# >Botão Excluir:
def excluir():
    selected_item = treev.selection()
    if len(selected_item) == 0:     # *Não foi escolhido nenhum item
        messagebox.showerror('ATENÇÃO ERRO', 'Selecione um ITEM da Tabela')
        return
    item = treev.item(selected_item)    # dictionary
    v_ID = item['values'][0]             # list
    try:
        res = messagebox.askquestion(
            'CONFIRMAR', 'O registro será EXCLUÍDO.\nDeseja continuar?')
        if res == 'yes':
            v_sql = f'DELETE FROM tb_contato WHERE ID = {v_ID}'
            Criadb('Cadastro').dml(v_sql)
            reset()
        else:
            reset()
            return
    except Error as err:
        print(f'ATENÇÃO ERRO: {err}')
    return


# >Botão Editar:
def editar():
    selected_item = treev.selection()
    if len(selected_item) == 0:     # *Não foi escolhido nenhum item
        messagebox.showerror('ATENÇÃO ERRO', 'Selecione um ITEM da Tabela')
        return
    item = treev.item(selected_item)    # dictionary
    v_ID = item['values'][0]             # list
    try:
        res = messagebox.askquestion(
            'CONFIRMAR', 'O registro será ALTERADO.\nDeseja continuar?')
        if res == 'yes':
            nome = txt_nome.get()
            fone = txt_fone.get()
            mail = txt_mail.get()
            end = txt_end.get()
            cid = txt_cid.get()
            uf = txt_uf.get()
            obs = txt_obs.get(1.0, 'end')

            v_sql = f'UPDATE tb_contato SET Nome = "{nome}", Fone = "{fone}", Email= "{mail}", Endereco= "{end}", Cidade= "{cid}", UF = "{uf}", Obs = "{obs}" WHERE ID = {v_ID}'
            Criadb('Cadastro').dml(v_sql)
            reset()
        else:
            reset()
            return
    except Error as err:
        print(f'ATENÇÃO ERRO: {err}')
    return


# >Botão Reset
def reset():
    limpatv(treev)
    conexao = Criadb('Cadastro')
    con = conexao.dml(v_sql)
    c = con.cursor()  # _ criar um cursor para receber a conexão
    # * execução da consulta (query) pelo cursor:
    c.execute('select * from tb_contato')
    res = c.fetchall()  # _ criar uma lista contendo todos os registros da tabela tb_contatos
    # v_con.close()  # _ fechar a conexão
    # - Inserindo (exibir) os registros na Treeview:
    for i in res:
        treev.insert('', 'end', values=[i[0], i[1],
                                        i[2], i[3], i[4], i[5], i[6], i[7]])
    # **Fechando o banco de dados:
    con.close()     # Fecha a conexão
    treev.bind('<<TreeviewSelect>>', item_selected) 
    limpatxt()
    return


# *Funções complementares:
def limpatxt():
    # **limpar os campos Entry e Text:
    txt_nome.delete(0, 'end')
    txt_fone.delete(0, 'end')
    txt_mail.delete(0, 'end')
    txt_end.delete(0, 'end')
    txt_cid.delete(0, 'end')
    txt_uf.delete(0, 'end')
    txt_obs.delete(1.0, 'end')
    # txt_nome.focus()
    treev.focus_set()
    return


def limpatv(arg):
    """
    Função para limpar a tela da TreeView antes de mostrar os dados

    :param arg: informa o nome da TreeView
    """
    treev = arg
    treev.delete(*treev.get_children())
    """
    * OU:
    for i in treev.get_children():
        treev.delete(i)
    """


def item_selected(evento):
    # global record

    for selected_item in treev.selection():
        item = treev.item(selected_item)    # dictionary
        record = item['values']             # list
        print(record)
        limpatxt()
        v_ID = record[0]
        txt_nome.insert(0, record[1])
        txt_fone.insert(0, record[2])
        txt_mail.insert(0, record[3])
        txt_end.insert(0, record[4])
        txt_cid.insert(0, record[5])
        txt_uf.insert(0, record[6])
        txt_obs.insert('end', record[7])
    return          #record


app = Tk()
app.title("Protótipo de Interface Gráfica - Cadastro")
app.geometry('1100x600')
app.configure(padx=2, pady=2, relief='sunken', border=1)

# -Selecionando o estilo dos widgets:
style = ttk.Style()
# temas = style.theme_names()  # ('clam', 'alt', 'default', 'classic')
style.theme_use('classic')
# tema = style.theme_use()
# print(f'\nOs temas disponíveis do sistema são: {temas}\nO tema em atual em uso é {tema}')

# -Criando uma janela panorâmica:
# , background="#0000ee", bg='blue'
pw = PanedWindow(app, orient='vertical', bg="grey")
pw.pack(fill='y', expand=0, side='top', padx=(2.5, 0))

# *Criando os Widgets da janela:

# -Widget quadros (Frame/LabelFrame):
# relief => flat(padrão), groove, raised, ridge, solid, ou sunken
lfr_contato = LabelFrame(app, text='CONTATOS',
                         relief='ridge',
                         borderwidth=1,
                         border=1,
                         font=('Ebrima', 10, 'bold'))
lfr_formulario = LabelFrame(app, text='EDITAR CONTATOS',
                            borderwidth=1, relief='ridge',
                            padx=10, pady=(0),
                            font=('Ebrima', 10, 'bold'))
lfr_pesquisar = LabelFrame(lfr_formulario, text='Pesquisar',
                           font=('Ebrima', 10, 'bold'),
                           relief='sunken', border=1,
                           borderwidth=1, labelanchor='n')
lfr_editar = LabelFrame(lfr_formulario, text='Editar',
                        font=('Ebrima', 10, 'bold'),
                        relief='sunken', border=1,
                        borderwidth=1, labelanchor='n')

fr_contato = Frame(lfr_contato, borderwidth=1, relief='sunken')
fr_btn_pesquisar = Frame(lfr_pesquisar, border=2,
                         borderwidth=2, relief='sunken')
fr_btn_inserir = Frame(lfr_editar, border=2, borderwidth=2, relief='sunken')
fr_btn_editar = Frame(lfr_editar, border=2, borderwidth=2, relief='sunken')
fr_btn_excluir = Frame(lfr_editar, border=2, borderwidth=2, relief='sunken')
fr_btn_reset = Frame(lfr_editar, border=2, borderwidth=2, relief='sunken')
fr_btn_sair = Frame(lfr_editar, border=2, borderwidth=2, relief='sunken')

# -Widget rótulo (Label):
lbl_nome = Label(lfr_formulario, text='Nome:', width=8, anchor='w')
lbl_fone = Label(lfr_formulario, text='Telefone:', width=8, anchor='w')
lbl_mail = Label(lfr_formulario, text='E-mail:', width=8, anchor='w')
lbl_end = Label(lfr_formulario, text='Endereço:', width=8, anchor='w')
lbl_cid = Label(lfr_formulario, text='Cidade:', width=8, anchor='w')
lbl_uf = Label(lfr_formulario, text='Estado:', width=8, anchor='w')
lbl_obs = Label(lfr_formulario, text='Nota:', width=4, anchor='w')
lbl_nome1 = Label(lfr_pesquisar, text='Nome:', width=5, anchor='w')

# -Widget texto (Entry):
txt_nome = Entry(lfr_formulario, width=25,
                 font=('Ebrima', 12), bd=1, justify='left', )
txt_fone = Entry(lfr_formulario, width=15,
                 font=('Ebrima', 12), bd=1, justify='left')
txt_mail = Entry(lfr_formulario, width=25,
                 font=('Ebrima', 12), bd=1, justify='left')
txt_end = Entry(lfr_formulario, width=30,
                font=('Ebrima', 12), bd=1, justify='left')
txt_cid = Entry(lfr_formulario, width=25,
                font=('Ebrima', 12), bd=1, justify='left')
txt_uf = Entry(lfr_formulario, width=2,
               font=('Ebrima', 12), justify='left')
txt_obs = Text(lfr_formulario, width=30, height=4,
               font=('Ebrima', 12))
txt_nome1 = Entry(lfr_pesquisar, width=19,
                  font=('Ebrima, 12'), justify='left')  # ***

# -Widget botões (Button):
btn_pesquisar = Button(fr_btn_pesquisar, text='Pesquisar',
                       width=10, bg='#b8b1e0', height=1,
                       font=('', '10', 'bold'), cursor='hand1',
                       border=3, relief='raised',
                       command=lambda: pesquisa(txt_nome1), pady=1)
btn_inserir = Button(fr_btn_inserir, text='Inserir', width=10, bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3,
                     relief='raised', command=inserir)
btn_editar = Button(fr_btn_editar, text='Alterar', width=10, bg='#b8b1e0',
                    font=('', '10', 'bold'), cursor='hand1', border=3,
                    relief='raised', command=editar)
btn_excluir = Button(fr_btn_excluir, text='Excluir', width=10,
                     bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3,
                     relief='raised', command=excluir)
btn_reset = Button(fr_btn_reset, text='Atualizar', width=10,
                   bg='#b8b1e0', font=('', '10', 'bold'),
                   cursor='hand1', border=3, relief='raised', command=reset)
btn_sair = Button(fr_btn_sair, text='Sair', width=10, bg='#b8b1e0',
                  font=('', '10', 'bold'), cursor='hand1', border=3,
                  relief='raised', command=exit)

# -Widget Treeview:

# -Definindo as colunas da Treeview:
colunas = ('id', 'nome', 'telefone', 'e-mail',
           'endereco', 'cidade', 'estado', 'observacao')

# -Widget Treeview:
treev = ttk.Treeview(fr_contato, columns=colunas,
                     show='headings', height=14)

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
scrollbarv = ttk.Scrollbar(fr_contato, orient='vertical', command=treev.yview)
scrollbarh = ttk.Scrollbar(
    fr_contato, orient='horizontal', command=treev.xview)
treev.configure(yscroll=scrollbarv.set)
treev.configure(xscroll=scrollbarh.set)

# *- ***** Definindo o tamanho das colunas *****
treev.column('id', width=35, minwidth=10, stretch=True, anchor='center')
treev.column('nome', width=170, minwidth=0, stretch=True)
treev.column('telefone', width=115, minwidth=0, stretch=True)
treev.column('e-mail', width=150, minwidth=0, stretch=True)
treev.column('endereco', width=200, minwidth=0, stretch=True)
treev.column('cidade', width=100, minwidth=0, stretch=True)
treev.column('estado', width=35, minwidth=0, stretch=True, anchor='center')
treev.column('observacao', width=230, minwidth=0, stretch=True)

# _Posicionando os Widgets quadros, rótulos, entrada de textos, botões e Treeview:

# *Quadros(Frame/LabelFrame):
lfr_contato.pack(fill='both', expand=True, anchor='s', side='top',
                 ipady=5, pady=5)  # side => top, bottom, left, or right
lfr_formulario.pack(fill='both', expand=True, side='top',
                    padx=(5, 0), pady=5, ipady=0,)
lfr_pesquisar.grid(column=4, row=5, columnspan=2, padx=(3, 0),
                   pady=(10, 10), sticky='w')
lfr_editar.grid(column=0, row=5, columnspan=4, padx=(6, 3),
                pady=(10, 10), ipady=5, sticky='w', ipadx=0)

fr_contato.pack(fill='both', expand=True, side='top',
                padx=(2, 0), pady=3, ipady=5,)
fr_btn_pesquisar.grid(column=3, row=0, rowspan=2, padx=5,
                      pady=(0, 5), sticky='nsew')
fr_btn_inserir.grid(column=0, row=0, padx=10, pady=(5, 0), sticky='nsew')
fr_btn_editar.grid(column=1, row=0, padx=5, pady=(5, 0), sticky='nsew')
fr_btn_excluir.grid(column=2, row=0, padx=10, pady=(5, 0), sticky='nsew')
fr_btn_reset.grid(column=3, row=0, padx=5, pady=(5, 0), sticky='nsew')
fr_btn_sair.grid(column=4, row=0, padx=10, pady=(5, 0), sticky='nsew')

# *Rótulos(Label):
lbl_nome.grid(column=0, row=2, pady=(10, 2))
lbl_fone.grid(column=0, row=3)
lbl_mail.grid(column=0, row=4)
lbl_end.grid(column=2, row=2, pady=(10, 2))
lbl_cid.grid(column=2, row=3)
lbl_uf.grid(column=2, row=4)
lbl_obs.grid(column=4, row=2, pady=(10, 2))
lbl_nome1.grid(column=0, row=0, padx=(6, 0), sticky='w')

# *Entrada de textos:
txt_nome.grid(column=1, row=2, padx=5, pady=(10, 2), sticky='w')
txt_fone.grid(column=1, row=3, padx=5, pady=2, sticky='w')
txt_mail.grid(column=1, row=4, padx=5, pady=2, sticky='w')
txt_end.grid(column=3, row=2, padx=5, pady=(10, 2), sticky='w')
txt_cid.grid(column=3, row=3, padx=5, pady=2, sticky='w')
txt_uf.grid(column=3, row=4, padx=5, pady=2, sticky='w')
txt_obs.grid(column=5, row=2, padx=(5, 0),
             pady=(10, 2), sticky='wn', rowspan=3)
txt_nome1.grid(column=0, row=1, padx=2, pady=5, sticky='nsew')

# *Botões:
btn_pesquisar.pack(anchor="center", ipady=1,
                   fill='x', side='left')
btn_inserir.pack()
btn_editar.pack()
btn_excluir.pack()
btn_reset.pack()
btn_sair.pack()

# *Treeview:
treev.grid(column=0, row=0, padx=(10, 10),
           pady=(3, 3), columnspan=6, sticky='nsew')
scrollbarv.grid(row=0, column=6, sticky='ns')
scrollbarh.grid(row=1, columnspan=6, sticky='ew')

# _Inserindo os registros de um banco de dados na  Treeview:
# *Criar o banco de dados, caso não exista:
v_sql = ("""
CREATE TABLE tb_contato(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome VARCHAR(30),
        Fone VARCHAR(14),
        Email VARCHAR(30),
        Endereco VARCHAR(30),
        Cidade VARCHAR(30),
        UF VARCHAR(2),
        Obs VARCHAR(500)
        );
        """)
vb_dados = Criadb('Cadastro')

# *Inserindo os dados na Treeview:
reset()

# *-Adicionando Widgets na PanedWindow:
pw.add(lfr_contato)
pw.add(lfr_formulario)

# -Incializando a janela:
mainloop()
