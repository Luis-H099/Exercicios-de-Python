from time import sleep
def grande(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando valores...')
    for valor in num:
        print(f'{valor} ',end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Eu recebi {cont} valores')
    print(f'E o maior número entre eles foi {maior}')


grande(2, 7, 8, 5, 12, 4)
grande(4, 7, 0)
grande(1, 2)
grande(6)
grande()