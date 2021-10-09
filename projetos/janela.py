#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import Button, Entry, Text, Frame, LabelFrame, PanedWindow, Label, ttk


app = tk.Tk()
app.title("Protótipo de janela")
app.geometry('1100x600')
app.configure(padx=2, pady=2, relief='flat', border=1)

# -Selecionando o estilo dos widgets:
style = ttk.Style()
# temas = style.theme_names()  # ('clam', 'alt', 'default', 'classic')
style.theme_use('classic')
# tema = style.theme_use()
# print(f'\nOs temas disponíveis do sistema são: {temas}\nO tema em atual em uso é {tema}')


# -Criando uma janela panorâmica:
pw = PanedWindow(app, orient='vertical')  # , background="#0000ee", bg='blue'
pw.pack(fill='both', expand=True, side='bottom')


# -Criando os quadros(frame):
# raised => flat(padrão), raised, sunken, solid
fr_sup = Frame(pw, borderwidth=2, relief='raised', border=1)
fr_sup.pack(fill='x', expand=True, anchor='n', side='top')

lf_centro = LabelFrame(pw, text='CONTATOS',
                       relief='sunken',
                       borderwidth=1,
                       border=1, 
                       font=('Ebrima', 10, 'bold'))
lf_centro.pack(fill='both', expand=True, anchor='s', side='top',
               ipady=125)  # side => top, bottom, left, or right

lf_inf = LabelFrame(pw, text='Inferior',
                    relief='sunken',
                    border=1,
                    borderwidth=1
                    )
lf_inf.pack(fill='both', expand=True, anchor='s', ipady=125)

fr_btn_sup = Frame(fr_sup, border=2, borderwidth=2, relief='sunken')
fr_btn_sup.pack(anchor='w')

fr_centro = Frame(lf_centro)
fr_centro.pack(fill='both', expand=True, side='top', padx=15, pady=10)

# -Criando os rótulos(label) e entrada de texto(Entry):
# -Definindo o quadro pai(master):
lf01 = fr_centro
lf02 = lf_inf

# -Elemento rótulo:
lbl_nome = Label(lf01, text='Nome: ', width=8, anchor='w')
lbl_fone = Label(lf01, text='Telefone: ', width=8, anchor='w')
lbl_mail = Label(lf01, text='E-mail: ', width=8, anchor='w')
lbl_end = Label(lf01, text='Endereço: ', width=8, anchor='w')
lbl_cid = Label(lf01, text='Cidade: ', width=8, anchor='w')
lbl_uf = Label(lf01, text='Estado: ', width=8, anchor='w')
lbl_obs = Label(lf01, text='Nota: ', width=4, anchor='w')

# -Elemento texto (Entry):
txt_nome = Entry(lf01, width=25, 
                 font=('Ebrima', 12), bd=1, justify='left')
txt_fone = Entry(lf01, width=15, 
                 font=('Ebrima', 12), bd=1, justify='left')
txt_mail = Entry(lf01, width=25, 
                 font=('Ebrima', 12), bd=1, justify='left')
txt_end = Entry(lf01, width=30, 
                 font=('Ebrima', 12), bd=1, justify='left')
txt_cid = Entry(lf01, width=25, 
                font=('Ebrima', 12), bd=1, justify='left')
txt_uf = Entry(lf01, width=2, 
               font=('Ebrima', 12), justify='left')
txt_obs = Text(lf01, width=29, height=4, 
               font=('Ebrima', 12), justify='left')

# -Posicionando os quadros e entrada de texto:
lbl_nome.grid(column=0, row=1)
txt_nome.grid(column=1, row=1, padx=5, pady=2, sticky='w')
lbl_fone.grid(column=0, row=2)
txt_fone.grid(column=1, row=2, padx=5, pady=2, sticky='w')
lbl_mail.grid(column=0, row=3)
txt_mail.grid(column=1, row=3, padx=5, pady=2, sticky='w')
lbl_end.grid(column=2, row=1)
txt_end.grid(column=3, row=1, padx=5, pady=2, sticky='w')
lbl_uf.grid(column=2, row=3)
txt_uf.grid(column=3, row=3, padx=5, pady=2, sticky='w')
lbl_obs.grid(column=4, row=1)
txt_obs.grid(column=5, row=1, padx=5, pady=2, sticky='wn', rowspan=3)

# -Criando os botões:
btn = Button(fr_btn_sup, text='TESTE', relief='raised', border=2)
btn.grid(column=0, row=0, ipadx=30, padx=2, pady=2, sticky='n')

btn2 = Button(lf_inf, text='Teste', relief='raised', border=5, borderwidth=3)
btn2.grid(column=0, row=0, ipadx=30, padx=30, pady=10, sticky='n')


# -Incializando a janela:
tk.mainloop()

# *****************************************************************************

# pw1 = PanedWindow(pw, orient='vertical', background="#0000ee", bg='blue')
# pw1.pack(fill='both', expand=True)

# pw2 = PanedWindow(app, orient='vertical', background="#0000ee", bg='green')
# pw2.pack(fill='both', expand=True, side=BOTTOM)

# global txt_nome, txt_fone, txt_mail, txt_end, txt_cid, txt_uf, txt_obs, lf01
# global btn_inserir, btn_editar, btn_excluir

# # *Frame para posicionar os botões, dentro da frame2:
# frm_btn = Frame(lf01, width=1050, height=50, relief="flat")

# reglist = [txt_nome, txt_fone, txt_mail, txt_end, txt_cid, txt_uf, txt_obs]

# frm_btn.grid(column=0, row=4, columnspan=6, pady=5)
# btn_inserir.place(x=250, y=10)
# btn_editar.place(x=390, y=10)
# btn_excluir.place(x=530, y=10)
# btn_reset.place(x=670, y=10)
# btn_inserir.grid(column=1, row=4, pady=5)
# btn_editar.grid(column=3, row=4, padx=2.5)
# btn_excluir.grid(column=5, row=4, padx=5)
# btn_reset.grid(column=3, row=5, padx=5, pady=10)

# btn1 = Button(lf_centro, text='teste', relief='raised', border=2)
# btn1.grid(column=0, row=0, ipadx=30, padx=30, pady=10, sticky='n')
