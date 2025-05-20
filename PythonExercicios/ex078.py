valores = []
for cont in range(0, 5):
    valores.append((int(input(f'Digite um valor para a posição {cont}: '))))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}... nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor}... e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
