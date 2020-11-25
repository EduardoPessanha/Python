from bibli.interface import texto
from bibli.numero import leiafloat, leiaint
from bibli.cor import corletra

print('Olá, Mundo!')
print(f'{corletra("az")}Já me livrei da maldição!{corletra()}')
leiaint('Digite um número: ')
leiafloat('Digite um número Real: ')
print()
texto('Isto é um Teste')
print()
texto('Este é um novo teste',simb='*')
