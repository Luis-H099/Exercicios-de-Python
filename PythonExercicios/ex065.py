n = int(input('Digite um número: '))
r = str(input('Deseja continuar? [S/N] '))
cont = 1
soma = 0 + n
media = maior = menor = 0
while r != 'n':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print('Você digitou {} números e a média foi {}'.format(cont,media))
