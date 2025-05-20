from random import choice
n1 = str(input('Primeira Opção: '))
n2 = str(input('Segunda Opção: '))
n3 = str(input('Terceira Opção: '))
n4 = str(input('Quarta Opção: '))
n5 = str(input('Quinta Opção: '))
lista = (n1, n2, n3, n4, n5)
escolhido = choice(lista)
print('A opção escolhida foi {}'.format(escolhido))