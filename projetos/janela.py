#!/usr/bin/env python3
# -*-coding:UTF-8-*-
"""

Protótipo de layout de interface gráfica para cadastro de contatos

"""
from tkinter import Button, Entry, Text, Frame, LabelFrame
from tkinter import PanedWindow, Label, mainloop, Tk, ttk

"""Para verificar as fontes do sistema
from tkinter import font, Tk

root = Tk()
print(font.families())
"""

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
lfr_formulario = LabelFrame(app, text='EDITAR CONTATOS', borderwidth=1,
                            relief='ridge', padx=10, pady=(0), font=('Ebrima', 10, 'bold'))
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
btn_pesquisar = Button(fr_btn_pesquisar, text='Pesquisar', width=10, bg='#b8b1e0', height=1,
                       font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised',
                       command='lambda: pesquisa(treev, txt_nome1)', pady=1)
btn_inserir = Button(fr_btn_inserir, text='Inserir', width=10, bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3,
                     relief='raised', command='lambda: inserir(reglist)')
btn_editar = Button(fr_btn_editar, text='Alterar', width=10, bg='#b8b1e0',
                    font=('', '10', 'bold'), cursor='hand1', border=3,
                    relief='raised', command="lambda: dml('editar'), state='disabled'")
btn_excluir = Button(fr_btn_excluir, text='Excluir', width=10, bg='#b8b1e0',
                     font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised',
                     command="lambda: dml('excluir'), state='disabled'")
btn_reset = Button(fr_btn_reset, text='Atualizar', width=10, bg='#b8b1e0',
                   font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised',
                   command='atualiza')
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

# *PanedWindow:
pw.add(lfr_contato)
pw.add(lfr_formulario)

# -Incializando a janela:
mainloop()
