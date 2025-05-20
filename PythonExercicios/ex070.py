nome = ''
preco = s = maisdemil = cont = menor = 0
continuar = ''
barato = ''
print('-' * 37)
print('       LOJAS SUPER BARATÃO')
print('-' * 37)
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))
    cont += 1
    s += preco
    if preco > 1000:
        maisdemil += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar == 'N':
        break
print(f'O total de compras foi R${s:.2f}')
print(f'Temos {maisdemil} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')
