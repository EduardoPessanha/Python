from bibli.interface import menu, linha, calcohm
from time import sleep

item = [f"{'Ecolha a unidade para calcular':>32}".upper(),
        ' ', f"{'V = Tensão':>18}",
        f"{'I = Corrente':>20}",
        f"{'R = Resistência':>23}",
        f"{'S = Sair do sistema':>27}", ' ']
titulo = " Lei de Ohm em Corrente Contínua "

while True:
    opcao = menu(item, titulo, op='V/I/R/S')
    if opcao == 'S':
        print(linha('*'))
        print('Saindo do sistema... Até logo!')
        break
    print(calcohm(opcao))
    sleep(1)
