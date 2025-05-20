galera = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp not in 'Ss':
        break
print('-=' * 30)
print(f'Você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}Kg, de', end='')
for p in galera:
    if p[1] == maior:
        print(f' [{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg de', end='')
for p in galera:
    if p[1] == menor:
        print(f' [{p[0]}] ', end='')
print()
