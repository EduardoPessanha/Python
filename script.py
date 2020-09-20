from random import randint
# print(' ')
# print('Hello World!')
# print(' ')
jogador = vitoria = 0
tipo = ' '
while True:
    jogador = int(input('Digite um valor: '))    
    computador = randint(0, 10)
    total = jogador + computador
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR [P/I]? ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador Jogou {computador}. Total de {total}, ', end='')
    print('deu PAR' if total % 2 == 0 else 'deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:  # Deu PAR
            vitoria += 1
            tipo = ' '
            print('Você VENCEU !!!!')
        else:
            print(('Você PERDEU !!!!'))
            break
    elif tipo == 'I':
        if total % 2 == 1:  # Deu ÍMPAR
            vitoria += 1
            tipo = ' '
            print('Você VENCEU !!!!')
        else:
            print('Você PERDEU !!!!')
            break
    print('Vamos jogar outra vez ...')  
