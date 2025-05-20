soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n // 2 == 0:
        cont += 1
        soma += n
print('Você informou {} números pares, e a soma deles é {}'.format(cont, soma))
