from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('         JOGA NA MEGA SENA ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quant} JOGOS =-=-=-')
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
sleep(0.5)
print('-=-=-=-= < BOA SORTE! > -=-=-=-=')


