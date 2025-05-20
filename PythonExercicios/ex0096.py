def calculo(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m²')


print(' CONTROLE DE TERRENOS')
print('-' * 40)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
calculo(a, b)