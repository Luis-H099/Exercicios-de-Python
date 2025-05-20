matriz = [[], [], []]
spar = mai = scol = 0
for c in range(0,3):
    for b in range(0,3):
        n = int(input(f'Digite um valor para [{c}, {b}]: '))
        matriz[c].append(n)
        if n % 2 == 0:
            spar += n
print('-=' * 30)
for c in range(0,3):
    for b in range(0,3):
        print(f'[{matriz[c][b]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares são {spar}')
for c in range(0,3):
    scol += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c] > mai:
        mai = matriz [1][c]
print(f'O maior valor da segunda coluna é {mai}')