from bibli.numero import leiafloat


def linha(simb='-', tam=40):
    return simb * tam


def texto(msg='', simb='-'):
    tam = len(msg) + 8
    print(linha(simb, tam))
    # print(f'{simb}{msg.upper().center(tam-2)}{simb}')
    print(msg.upper().center(tam))
    print(linha(simb, tam))
    return


def menu(lista='', titulo='menu principal', op=' '):
    """ Recebe os itens do menu
    :param lista: lista contendo os itens do menu
    :param titulo: Título do menu
    :param op: opções disponíveis
    :return: retorna a opção escolhida no menu
    """
    cab(titulo, '*')
    print(linha('*'))
    for item in lista:
        print(f'{"*":<3}{item}{"*":>{37 - len(item)}}')
    print(linha('*'))
    if op != ' ':
        while True:
            opcao = str(input(f'Escolha a Sua opção ({op}): ')).upper()
            if opcao not in op:
                print(f'\033[1;31mERRO: Opção \"INVÁLIDA\". Tente outra vez.\033[m')
            else:
                break
    else:
        opcao = str(input(f'Escolha a Sua opção: '))
    return opcao


def cab(txt='', simb='=', tam=40):
    """

    :param txt: texto a ser formatado
    :param simb: simbolo para usar nas linhas
    :param tam: tamanho da linha
    :return:
    """
    print(linha(simb, tam))
    print(txt.upper().center(tam))
    print(linha(simb, tam))
    return


def calcohm(op=''):
    res = 0
    if op == 'V':
        i = leiafloat('Valor da corrente em Ampere: ')
        r = leiafloat('Valor da resistência em Ohm:')
        v = i * r
        res = f'O valor da tensão é {v:.2f} Volts'
    elif op == 'I':
        v = leiafloat('Valor da tensão em Volts: ')
        r = leiafloat('Valor da resistência em Ohm:')
        i = v / r
        res = f'O valor da corrente é {i:.2f} Amperes'
    elif op == 'R':
        i = leiafloat('Valor da corrente em Ampere: ')
        v = leiafloat('Valor da tensão em Volts:')
        r = v / i
        res = f'O valor da resistência é {v:.2f} Ohms'
    return res
