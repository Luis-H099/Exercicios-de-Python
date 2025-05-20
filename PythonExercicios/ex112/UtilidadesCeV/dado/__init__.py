def leiadinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',','.')
        if n.isalpha() or n.strip() == '':
            print('\033[0;31mERRO, Digite um número inteiro válido.\033[m')
        else:
            ok = True
    return float(n)