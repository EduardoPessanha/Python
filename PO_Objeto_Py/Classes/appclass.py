#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    _A programação orientada a objetos (POO) é um paradigma de programação
    _baseado no conceito de " objetos ", que podem conter dados e código:
    _dados na forma de campos (geralmente conhecidos como atributos ou
    _propriedades) e código, na forma de procedimentos (freqüentemente
    _conhecido como métodos).

    _Uma característica dos objetos é que os próprios procedimentos de um
    _objeto podem acessar e, muitas vezes, modificar os campos de dados de si
    _mesmo (os objetos têm uma noção de this ou self) Na POO, os programas de
    _computador são projetados a partir de objetos que interagem uns com os
    _outros. As linguagens POO são diversas, mas as mais populares são
    _baseadas em classes , o que significa que os objetos são instâncias de
    _classes , que também determinam seus tipos.

    _Na programação orientada à objetos o foco é na criação de objetos que
    _contem tanto os dados quanto as funcionalidades.

    _Em Python, todo valor é na verdade um objeto. Seja uma string, uma lista,
    _ou mesmo um inteiro, todos são objetos. Programas manipulam esses objetos
    _realizando computações diretamente com eles ou chamando os seus métodos
    _(ou seja, pedindo que esses objetos executem seus métodos).
    _Para ser mais específico, nós dizemos que um objeto possui um 'estado' e
    _uma coleção de métodos que ele pode executar. O 'estado' de um objeto
    _representa as coisas que o objeto sabe sobre si mesmo.
    _Por exemplo, um objeto tartaruga, possui um estado que representa a sua
    _posição, sua cor, sua direção, etc. Cada tartaruga também tem a
    _capacidade de se mover para a frente, para trás, ou virar para a direita
    _ou esquerda. Cada tartaruga é diferente pois, embora sejam todas
    _tartarugas, cada uma tem um estado diferente (como posições diferentes,
    _ou orientações, etc)

Começando a estudar Class .........

    _As definições de classes podem aparecer em qualquer lugar em um programa,
    _mas são geralmente perto do início (após os comandos import). As regras de
    _sintaxe para a definição de uma classe são as mesmas de outros comandos
    _compostos. Há um cabeçalho que começa com a palavra-chave 'class', seguido
    _pelo nome da classe e terminando com dois pontos.

"""

# from tkinter import mainloop, messagebox, Tk
# from tkinter.ttk import Style
# from sqlite3 import Error, connect
# from os import path, system

# _Toda classe deve ter um método com o nome especial __init__. Este método de
# _inicialização, muitas vezes referido como o 'construtor', é chamado
# _automaticamente sempre que uma nova instância da Classe é criada. Ela dá ao
# _programador a oportunidade de configurar os atributos necessários dentro da
# _nova instância, dando-lhes seus estados/valores iniciais. O parâmetro self
# _(qe poderia ser qualquer outro nome, mas ninguém nunca faz!) é definido
# _automaticamente para referenciar o objeto recém-criado que precisa ser
# _inicializado.


class Ponto:
    """
    Criando a minha primeira Class!!!!!

    Classe para representar e/ou manipular coordenadas x, y
    """

    def __init__(self) -> None:   # *Construtor
        """
        ->Cria um novo ponto na origem
        """
        self.initx = 0
        self.inity = 0


p = Ponto()  # *instancie um objeto do tipo Ponto (Instanciar=criar um objeto)
q = Ponto()  # *e faça um segundo ponto


print("\nNada parece ter acontecido com os pontos\n")
print(p, 'id:', id(p), '\n')
print(q, 'id:', id(q), '\n')
print(p is q)

"""
Durante a inicialização dos objetos, criamos dois atributos chamados x e y
para cada um, e ambos com o valor 0.
Podemos observar que quando executamos o programa, nada acontece.
Felizmente este não é bem o caso. De fato, dois Pontos foram criados, cada um
com coordenadas x e y com valor 0. No entanto, como nós não pedimos aos pontos
para fazerem alguma coisa, não vemos resultado algum.

As variáveis p e q recebem referências a dois novos objetos Ponto. Uma função
Ponto() que cria uma nova instância do objeto é chamado de construtor, e cada
classe fornece automaticamente uma função construtora que tem o mesmo nome da
classe.
"""




















# def mostrar(self):
#     resp = (self.initx**2 + self.inity**2)**0.5
#     return resp
#     # print(f"\nO banco de dados {self.arq} não exite!!!!\n")


# _Referências:
# *https://www.youtube.com/watch?v=RhtsCbKyYoA&t=1110s
# *https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
