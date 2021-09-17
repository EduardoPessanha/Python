# -*- coding: utf-8 -*-
"""
    Agenda de Telefone e endereço
    Versão inicial
"""

import libagenda as lb
from tkinter import *

tela = Tk()
tela.title('Minha Agenda')
tela.configure(padx=5, pady=10, borderwidth=4,
               relief='groove', background='#cccccc')
tela.geometry('1100x640')

"""
    -Definindo os elementos da tela:
"""
# _ Elementos do formulário:

# * Elemento LabelFrame:
frame1 = LabelFrame(tela, text='Contatos', font=(
    'Ebrima', 10, 'bold'), width=1050, height=260)
frame2 = LabelFrame(tela, text='Contatos',
                    font=('Ebrima', 10, 'bold'), width=1050, height=80,pady=10)
frame3 = LabelFrame(tela, text='Pesquisar Contatos', font=(
    'Ebrima', 10, 'bold'), width=1050, height=80, padx=136, pady=10)

# * Posicionando os LabelFrames:
frame1.grid(column=0, row=0, padx=10, pady=5, sticky='w')
frame2.grid(column=0, row=1, padx=10, pady=5, sticky='w')
frame3.grid(column=0, row=2, padx=10, pady=5, sticky='w')

# * Elementos do frame1 -> Treeview:
lb.tvw(frame1)      # _ Gera a Treeview

# * Elementos do frame2:
lb.lfr2(frame2)     # _ Gera os elementos do LabelFrame 2

# * Elementos do frame3:
lb.lfr3(frame3)     # _ Gera os elementos do LabelFrame3

tela.mainloop()
