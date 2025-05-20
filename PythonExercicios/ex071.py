cont50 = cont20 = cont10 = cont1 = 0
print('=' * 40)
print('        BANCO CEV')
print('=' * 40)
v = int(input('Quanto deseja sacar?: '))
while True:
    if v >= 50:
        v -= 50
        cont50 += 1
    elif v >= 20:
        v -= 20
        cont20 += 1
    elif v >= 10:
        v -= 10
        cont10 += 1
    elif v >= 1:
        v -= 1
        cont1 += 1
    else:
        break
if cont50 + cont20 + cont10 + cont1 > 0:
    if cont50 > 0:
        print(f'Total de {cont50} cédulas de R$50')
    if cont20 > 0:
        print(f'Total de {cont20} cédulas de R$20')
    if cont10 > 0:
        print(f'Total de {cont10} cédulas de R$10')
    if cont1 > 0:
        print(f'Total de {cont1} cédulas de R$1')
else:
    print('Você não sacou nenhum dinheiro!')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
