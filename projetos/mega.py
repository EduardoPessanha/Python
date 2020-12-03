from bibli.cor import corletra
from bibli.interface import texto
from bibli.numero import leiaint
from bibli.uteis import mega
from time import sleep

print(corletra('az'))
texto('Palpites para a Mega Sena', simb='=')
print(corletra())

contador = 1
jogos = leiaint('Quantos jogos você quer sortear? ')
print()

print('\033[1;34m*=' * 3, f' SORTEANDO {jogos} JOGOS ', '*=' * 3, '\033[m')
while contador <= jogos:
    print(f'Jogo {contador} -> {mega()}')
    sleep(1)
    contador += 1

print(corletra('az'))
print(f"\n{'>->>-> BOA SORTE! <-<<-'.center(33)}")
print(corletra())
