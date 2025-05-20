print('GERADOR DE PA')
print('-=' * 20)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
c = 1
termo = n1
while c <= 10:
    print('{} ➔ '.format(termo),end='')
    termo += n2
    c += 1
print('Fim')
