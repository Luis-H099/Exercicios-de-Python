print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➔ '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Se teve no total {} termos'.format(total))
print('FIM')