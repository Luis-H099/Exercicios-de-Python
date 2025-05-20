matriz = [[], [], []]
for c in range(0,3):
    for b in range(0,3):
        n = int(input(f'Digite um valor para [{c}, {b}]: '))
        matriz[c].append(n)
print('-=' * 30)
for c in range(0,3):
    for b in range(0,3):
        print(f'[{matriz[c][b]:^5}]', end='')
    print()
