alunos = list()
estudante = list()
tot = 0
while True:
    estudante.append(str(input('Nome: ')))
    estudante.append(float(input('Nota 1: ')))
    estudante.append(float(input('Nota 2: ')))
    alunos.append(estudante[:])
    estudante.clear()
    tot += 1
    esc = str(input('Quer continuar? [S/N] '))
    if esc not in 'Ss':
        break
print('-=' * 30)
print('No.    NOME        MÉDIA   ')
print('-' * 26)
for c in range(0, tot):
    print(f'{c:<5}  {alunos[c][0]:<10}     {(alunos[c][1] + alunos[c][2]) / 2:<5}')
print('-' * 26)
while True:
    mostrar = int(input('Mostrar notas de qual alunos?[999 interrompe] '))
    if mostrar == 999:
        break
    else:
        print('-' * 30)
        print(f'Notas de {alunos[mostrar][0]} são [{alunos[mostrar][1]}, {alunos[mostrar][2]}]')
        print('-' * 30)
print('<<< VOLTE SEMPRE >>>')
