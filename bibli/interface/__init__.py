def linha(simb='-', tam=40):
    return simb * tam


def texto(msg='', simb='-'):
    tam = len(msg)+8
    print(linha(simb, tam))
    # print(f'{simb}{msg.upper().center(tam-2)}{simb}')
    print(msg.upper().center(tam))
    print(linha(simb, tam))
    return
