total = 0
cont = -1
n = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    total += n
    soma = total - 999
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
