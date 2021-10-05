```py
import tkinter as tk
root = tk.Tk()
txt = tk.Text(root, height=5, width=25, bg='lightblue')
txt.insert('1.0', 'this is a Text widget')
tk.Button(root, text='quit', command=quit).pack(side="bottom")
txt.pack(fill=tk.BOTH,expand=True)
root.mainloop()
```
"""
O lambda que significa:

Quando você tem que passar argumentos para a própria função, você não pode evitar parentheses().
Portanto, no caso de buttons, lambda basicamente atrasa a execução da função até que o usuário clique no botão, criando outra função no local, que não é chamada até que o botão seja realmente clicado. Conseqüentemente, a função não é executada, onde é fornecida como commandao Button.
"""


"""
A solução mais simples é usar uma janela panorâmica, que tem esse recurso embutido. Uma janela panorâmica é usada como um quadro, mas em vez de usar packou gridadicionar widgets a ela, você usa o addmétodo. O widget colocará um separador entre os widgets, permitindo que você ajuste o tamanho relativo. As janelas de painéis têm orientação horizontal ou vertical.

Exemplo
Este exemplo assume python 2.x. Para 3.x você só precisa alterar as importações.

Nota: tanto o tkinter quanto o ttk fornecem uma janela panorâmica (PanedWindow). O exemplo a seguir usa o de ttk que, sem dúvida, parece um pouco melhor.
"""

```
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TESTE")

# the main window is divided into left and right sections,
# and the sidebar is divided into a top and bottom section.
# a janela principal é dividida nas seções esquerda e direita,
# e a barra lateral é dividida em uma seção superior e inferior.
pw = ttk.PanedWindow(orient="horizontal")
sidebar = ttk.PanedWindow(pw, orient="vertical")
main = tk.Frame(pw, width=400, height=400, background="black")
sidebar_top = tk.Frame(sidebar, width=200, height=200, background="gray")
sidebar_bottom = tk.Frame(sidebar, width=200, height=200, background="white")

# add the paned window to the root
pw.pack(fill="both", expand=True)

# add the sidebar and main area to the main paned window
pw.add(sidebar)
pw.add(main)

# add the top and bottom to the sidebar
sidebar.add(sidebar_top)
sidebar.add(sidebar_bottom)

root.mainloop()
```
Python - Tkinter PanedWindow
Anúncios


 Página anteriorPróxima página  
Um PanedWindow é um widget de contêiner que pode conter qualquer número de painéis, organizados horizontal ou verticalmente.

Cada painel contém um widget e cada par de painéis é separado por uma faixa móvel (por meio de movimentos do mouse). Mover uma faixa faz com que os widgets em ambos os lados da faixa sejam redimensionados.

Sintaxe
Aqui está a sintaxe simples para criar este widget -

w = PanedWindow( master, option, ... )
Parâmetros
master - representa a janela principal.

options - Aqui está a lista das opções mais comumente usadas para este widget. Essas opções podem ser usadas como pares de valores-chave separados por vírgulas.

Sr. Não.	Opção e descrição
1	
bg

A cor do controle deslizante e das pontas de seta quando o mouse não está sobre eles.

2	
bd

A largura das bordas 3-d em torno de todo o perímetro da depressão e também a largura dos efeitos 3-d nas pontas das setas e no controle deslizante. O padrão é sem borda ao redor da calha e uma borda de 2 pixels ao redor das pontas de seta e controle deslizante.

3	
largura da fronteira

O padrão é 2.

4	
cursor

O cursor que aparece quando o mouse está sobre a janela.

5	
maçaneta

O padrão é 8.

6	
tamanho do punho

O padrão é 8.

7	
altura

Sem valor padrão.

8	
orientar

O padrão é HORIZONTAL.

9	
alívio

O padrão é FLAT.

10	
sashcursor

Sem valor padrão.

11	
caixinha

O padrão é RAISED.

12	
largura da faixa

O padrão é 2.

13	
showhandle

Sem valor padrão.

14	
largura

Sem valor padrão.

Métodos
Os objetos PanedWindow têm estes métodos -

Sr. Não.	Métodos e Descrição
1	
adicionar (filho, opções)

Adiciona uma janela filha à janela com painéis.

2	
get (startindex [, endindex])

Este método retorna um caractere específico ou um intervalo de texto.

3	
config (opções)

Modifica uma ou mais opções de widget. Se nenhuma opção for fornecida, o método retorna um dicionário contendo todos os valores das opções atuais.

Exemplo
Experimente o seguinte exemplo você mesmo. Veja como criar um widget de 3 painéis -

from Tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()
Quando o código acima é executado, ele produz o seguinte resultado -

TK PanedWindow


https://www.tutorialspoint.com/python/tk_panedwindow.htm