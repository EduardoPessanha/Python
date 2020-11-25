from bibli.cor import *


def leiaint(texto):
	"""
	-> Lê um valor de entrada e faz a validação
	para aceitar apenas um valor numérico.
	:param texto: recebe o valor a ser validada.
	:return: retorna um valor Inteiro.
	"""
	while True:
		try:
			num = int(input(texto))
		except (ValueError, TypeError):
			print(f'{corletra("vm")}ERRO! Digite um número \"Inteiro\" válido!.{corletra()}')
			continue
		except (KeyboardInterrupt, EOFError):
			print(f'\n{corletra("az")}O usuário preferiu não digitar esse valor!{corletra()}')
			return 0
		else:
			return num


def leiafloat(texto):
	"""
	-> Lê um valor de entrada e faz a validação
	para aceitar apenas um valor Real.
	:param texto: recebe o valor a ser validado.
	:return: retorna um valor Real.
	"""
	while True:
		try:
			num = str(input(texto)).replace(',', '.')
			num = float(num)
		except (ValueError, TypeError):
			print(f'{corletra("vm")}ERRO! Digite um número \"Real\" válido!.{corletra()}')
			continue
		except (KeyboardInterrupt, EOFError):
			print(f'\n{corletra("az")}O usuário preferiu não digitar esse valor!{corletra()}')
			return 0
		else:
			return num
