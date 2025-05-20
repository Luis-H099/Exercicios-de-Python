idade = homens = mulheresnovas = maiores = 0
sexo = ''
continuar = ''
while True:
    print('-' * 20)
    print('    CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    continuar = str(input('Quer continuar? [S/N]: '))
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresnovas += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresnovas} mulheres com menos de 20 anos')
