from bibli.uteis import moeda
from bibli.Ajuda import pyhelp
from bibli.cor import corletra
from bibli.interface import texto
from bibli.numero import leiafloat, leiaint

print('Olá, Mundo!')
print(f'{corletra("az")}Já me livrei da maldição!{corletra()}')
leiaint('Digite um número: ')
leiafloat('Digite um número Real: ')
print()
texto('Isto é um Teste')
print()
texto('Este é um novo teste', simb='*')
print(moeda())
