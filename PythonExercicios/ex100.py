from random import randint
from time import sleep
def sortear(lista):
    print('Sorteando 5 valores da lista: ', end ='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {num}, temos {soma}')


num = list()
sortear(num)
somaPar(num)