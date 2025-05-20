maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Quanto pesa a {}º pessoa?: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('O maior peso entre todos foi de {}kg'.format(maior))
print('O menor peso entre todos foi de {}kg'.format(menor))