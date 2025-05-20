def contador(a, b, c):
    if c == 0:
        c = -1
    print(f'Contagem de {a} até {b} contando de {c} em {c}')
    for d in range(a, b, c):
        print(f' {d}', end='')
        sleep(0.2)
    print(' FIM!')


from time import sleep
print('=' * 30)
contador(1, 10, 1)
print('=' * 30)
contador(10, 0, -2)
print('=' * 30)
print('AGORA É A SUA VEZ DE PERSONALIZAR A CONTAGEM!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
print('=' * 30)
contador(a, b, c)