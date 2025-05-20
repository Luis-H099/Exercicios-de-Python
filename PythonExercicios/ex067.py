n = int(input('Digite um valor para ver sua tabuada: '))
while True:
    if n < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 20)
    n = int(input('Digite outro valor para ver sua tabuada: '))
print('Finalizando Programa...Volte sempre!')
