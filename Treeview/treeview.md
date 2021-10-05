<CENTER>

# Tkinter Treeview

</CENTER>  

Resumo : neste tutorial, você aprenderá sobre o widget Tkinter Treeview e como usá-lo para exibir dados tabulares e hierárquicos.

## Introdução ao widget Tkinter Treeview  
Um widget Treeview permite exibir dados em estruturas tabulares e hierárquicas.

Para criar um widget Treeview, você usa a ttk.Treeview classe:

tree = ttk.Treeview(container, **options)  

Linguagem de código:  Python  ( python )

Um widget Treeview contém uma lista de itens. Cada item possui uma ou mais colunas.

A primeira coluna pode conter texto e um ícone que indica se você pode expandi-la ou não.

As colunas restantes contêm valores que você deseja exibir para cada linha.

A primeira linha da Treeview consiste em títulos que identificam cada coluna por seu nome.

## Usando Tkinter Treeview para exibir dados tabulares

O programa a seguir mostra como usar o widget Treeview para exibir dados tabulares:

```py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# columns
columns = ('#1', '#2', '#3')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('#1', text='First Name')
tree.heading('#2', text='Last Name')
tree.heading('#3', text='Email')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# adding data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()

```

Saida:  

![img](Tkinter-Treeview-Tabular-Data.png)  

Como funciona.

Primeiro, importe o módulo tkinter, o submódulo ttk e o showinfo de tkinter.messagebox:

```py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
```

Em segundo lugar, crie a janela raiz (root), defina seu título e tamanho: 

```py
root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')
```

Terceiro, defina os identificadores para colunas:

```py
columns = ('#1', '#2', '#3')
```
Quarto, crie un widget Tkinter Treeview:

```py
tree = ttk.Treeview(root, columns=columns, show='headings')
```

Neste código, passamos as colunas para a opção de colunas.

O show = ’header’ oculta a primeira coluna (coluna #0) da Treeview.

A opção show aceita um dos seguintes valores:


*  'tree' – mostra a coluna# 
*  'heading' – mostra a linha do cabeçalho
*  'tree headings' – mostra a coluna#0 e a linha do cabeçalho. Este é o valor padrão
*  ' ' – não mostra a coluna #0 ou a linha do cabeçalho


Quinto, especifique os títulos das colunas:  

```py
tree.heading('#1', text='First Name')
tree.heading('#2', text='Last Name')
tree.heading('#3', text='Email')
```  

Sexto, gere uma lista de tuplas para exibição na Treeview:  

```py
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
```  


Sétimo, crie novos itens, um por um, usando o insert(), método do objeto Treeview:  

```py
for contact in contacts:
    tree.insert('', tk.END, values=contact)
```  


Oito, defina uma função para lidar com o <> evento. Quando você seleciona um ou mais itens, o programa mostra uma caixa de mensagem:  

```py
# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)
```  

Nono, coloque o widget Treeview na janela raiz(root):  

```py
tree.grid(row=0, column=0, sticky='nsew')
```  

Décimo, adicione uma barra de rolagem vertical ao widget Treeview:  

```py
# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
```  

Por fim, exiba a janela raiz(root):  

```py
# run the app
root.mainloop()
```  

##  Usando Tkinter Treeview para exibir dados hierárquicos  

O programa a seguir ilustra como usar o widget TreeView para exibir dados hierárquicos:  

```py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create root window
root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('400x200')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree.heading('#0', text='Departments', anchor='w')


# adding data
tree.insert('', tk.END, text='Administration', iid=0, open=False)
tree.insert('', tk.END, text='Logistics', iid=1, open=False)
tree.insert('', tk.END, text='Sales', iid=2, open=False)
tree.insert('', tk.END, text='Finance', iid=3, open=False)
tree.insert('', tk.END, text='IT', iid=4, open=False)

# adding children of first node
tree.insert('', tk.END, text='John Doe', iid=5, open=False)
tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
tree.move(5, 0, 0)
tree.move(6, 0, 1)

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()
```  

Saída:

![img](Tkinter-Treeview-Hierarchical-Data.png)

Como funciona.

Vamos nos concentrar na parte do widget Treeview.

First, create a Treeview widget and set its heading.

```py
tree = ttk.Treeview(root)
tree.heading('#0', text='Departments', anchor='w')
```

This Treeview widget has only one column.

Second, add items to the TreeView widget:
```py
tree.insert('', tk.END, text='Administration', iid=0, open=False)
tree.insert('', tk.END, text='Logistics', iid=1, open=False)
tree.insert('', tk.END, text='Sales', iid=2, open=False)
tree.insert('', tk.END, text='Finance', iid=3, open=False)
tree.insert('', tk.END, text='IT', iid=4, open=False)
```  

Cada item é identificado por um iid. Se você pular o iid, o método de inserção irá gerar um automaticamente. Neste caso, você precisa ter explícito iid para adicionar itens filho.  

Terceiro, adicione dois itens filho ao item com iid 0 usando os métodos insert() e move():  

```py
# adding children of first node
tree.insert('', tk.END, text='John Doe', iid=5, open=False)
tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
tree.move(5, 0, 0)
tree.move(6, 0, 1)
```

Finalmente, coloque o widget Treeview na janela raiz(root) e exiba-o.

```py
# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()
```  

Resumo:  
*  Use um widget Tkinter Treeview para exibir dados tabulares e hierárquicos.  
  

Referência:  
<https://www.pythontutorial.net/tkinter/tkinter-treeview/>  
