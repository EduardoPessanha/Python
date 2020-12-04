def moeda(n='0', tipo='R$'):
    """
    -> formata um valor no padrão monetário definido
    no tipo, se tipo não for definido retorna no padrão
    monetário brasileiro -> "R$"
    :param n: valor a ser formatado
    :param tipo: formato monetário a ser usado
    :return: valor formatado
    """
    while True:
        try:
            if n == '0':
                num = str(input('Digite o valor: ')).replace(',', '.')
            else:
                num = str(n).replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: O valor \"{num}\" não é válido! Tente outra vez.\033[m')
            if n != '0':
                n = '0'
            continue
        except (KeyboardInterrupt, EOFError):
            print(
                f'\n\033[1;34mO usuário preferiu não digitar esse valor!\033[m')
            return 0
        else:
            if tipo == 'R$':
                num = f'{num:.2f}'.replace('.', ',')
                return f"{tipo} {num}"
            else:
                return f'{tipo} {num:.2f}'


def mega():
    from random import randint
    sorteio = list()
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            contador += 1
        if contador >= 6:
            break
    sorteio = sorted(sorteio)
    # sorteio.sort()
    return sorteio
