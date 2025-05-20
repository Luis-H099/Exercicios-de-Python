num = list()
while True:
    n = int(input('Digite um Valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]  '))
    if r in 'Nn':
        break
print('-=' * 30)
num.sort()
print(f'Você digitou os valores {num}')