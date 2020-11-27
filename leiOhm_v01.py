titulo = "\033[1;7;33m Lei de Ohm em Corrente Contínua \033[m"
print(f"\n{titulo:^52}\n")
fim = ' '
linha = '\033[1;34m-=\033[m' * 21
while fim not in 'N':
    print('''****************************************
*  Qual a unidade você quer calcular:  *
*                                      *
*           V = Tensão                 *
*           I = Corrente               *
*           R = Resistência            *
*                                      *
****************************************''')  # Acrescentar 'X' = Sair
    while True:
        opcao = str(input('Escolha a sua opção (V/I/R): ')).upper().strip()[0]
        if opcao not in 'VIR':
            print('Entrada INVÁLIDA.', end=' ')
        else:
            break
    if opcao == 'V':
        print(f'\n{linha}\n')
        I = float(input('Informe o valor da corrente em Aperes: '))
        R = float(input('Informe o valor da resistência em Ohms: '))
        V = I * R
        print(f'O valor da tensão é {V:.2f} Volts\n')
        print(f'{linha}\n')
    elif opcao == 'I':
        print(f'\n{linha}\n')
        V = float(input('Informe o valor da tensão em Volts: '))
        R = float(input('Informe o valor da resistência em Ohms: '))
        I = V / R
        print(f'O valor da corrente é {I:.2f} Aperes\n')
        print(f'{linha}\n')
    elif opcao == 'R':
        print(f'\n{linha}\n')
        V = float(input('Informe o valor da tensão em Volts: '))
        I = float(input('Informe o valor da corrente em Aperes: '))
        R = V / I
        print(f'O valor da resistência é {R:.2f} Ohms\n')
        print(f'{linha}\n')
    while True:
        fim = str(input('Deseja continuar (S/N): ')).upper().strip()[0]
        if fim not in 'SN':
            print('Opção INVÁLIDA.', end=' ')
        else:
            break
    if fim == 'N':
        print()
        break
    else:
        print(f'{linha}\n')
