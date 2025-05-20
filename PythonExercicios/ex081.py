lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    sn = str(input('Quer continuar? [S/N] '))
    if sn not in 'Ss':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores digitados em forma decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 faz parte da lista!')