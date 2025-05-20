from random import randint
cont = n = computador = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
p = ''
while p in 'PI':
    computador = randint(0, 10)
    n = int(input('Diga um valor: '))
    p = str(input('Par ou Ímpar? [P/I] '))
    s = n + computador
    print('-' * 20)
    if s % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {computador}. Total de {s} DEU PAR!')
    else:
        print(f'Você jogou {n} e o computador jogou {computador}. Total de {s} DEU ÍMPAR!')
    print('-' * 20)
    if p == 'P' and s % 2 == 0:
        print('Você VENCEU!')
        cont += 1
    elif p == 'I' and s % 2 == 1:
        print('Você VENCEU!')
        cont += 1
    else:
        break
    print('Vamos jogar novamente!')
print(f'GAMEOVER! Você venceu {cont}')
