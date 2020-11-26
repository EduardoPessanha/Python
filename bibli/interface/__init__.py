def linha(simb='-', tam=40):
	return simb * tam


def texto(msg='', simb='-'):
	tam = len(msg) + 8
	print(linha(simb, tam))
	# print(f'{simb}{msg.upper().center(tam-2)}{simb}')
	print(msg.upper().center(tam))
	print(linha(simb, tam))
	return


def menu(lista=''):
	""" Recebe os itens do menu
	:param lista: lista contendo os itens do menu
	:return: retorna a opção escolhida no menu
	"""
	cab('menu principal', '*')
	print(linha('*'))
	for item in lista:
		print(f'{"*":<3}{item}{"*":>{37 - len(item)}}')
	print(linha('*'))
	opcao = str(input('Sua opção: '))
	return opcao


def cab(txt='', simb='=', tam=40):
	print(linha(simb))
	print(txt.upper().center(tam))
	print(linha(simb))
	return
