from time import sleep


def fundo(tipo=''):
    cf = {'': '\033[m',           # 0 - restaura cor padrão
          'br': '\033[1;7;30m',   # 1 - fundo branco
          'vm': '\033[1;30;41m',  # 2 - fundo vermelho
          'vd': '\033[1;30;42m',  # 3 - fundo verde
          'am': '\033[1;30;42m',  # 4 - fundo amarelo
          'az': '\033[1;30;44m',  # 5 - fundo azul
          'mg': '\033[1;30;45m',  # 6 - fundo magenta
          'ci': '\033[1;30;46m',  # 7 - fundo ciânico
          'cz': '\033[1;30;47m'   # 8 - fundo cinza
          }
    return cf[tipo]


def cab(msg, cor=''):
    c = len(msg)
    print(fundo(cor), end='')
    print('*' * (c + 4))
    print(f'* {msg} *')
    print('*' * (c + 4))
    print(fundo(), end='')


def manual(func):
    cab(f"Acessando o manual do comando '{func}'", 'az')
    sleep(1)
    print(fundo('br'))
    help(func)
    print(fundo(), end='')
    sleep(6)


def pyhelp():
    while True:
        cab(' SISTEMA DE AJUDA PyHELP ', 'vd')
        nome = str(input('Função da biblioteca -> '))
        if nome.upper() == 'FIM':
            break
        manual(nome)
    cab(' ATÉ LOGO!', 'vm')


def main():
    pyhelp()
    return


if __name__ == '__main__':
    main()
