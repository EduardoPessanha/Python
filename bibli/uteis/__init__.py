def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (taxa * preco / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


def moeda(tipo='R$'):  # Analisar e melhorar essa função!!
    """
    -> formata um valor no padrão monetário definido
    no tipo, se tipo não for definido retorna no padrão
    monetário brasileiro -> "R$"
    :param tipo: formato monetário a ser usado
    :return: valor formatado
    """
    # Reformular para receber 2 parametros: 'n' e 'tipo', caso não seja informado o parametro 'n', perguntar qual o valor a ser formatado.
    while True:
        try:
            num = str(input('Digite o valor: ')).replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: O valor \"{num}\" não é válido! Tente outra vez.\033[m')
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
