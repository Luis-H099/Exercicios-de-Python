soma = 0
velho = 0
novo = 0
cont = 0
nomevelho = ''
for c in range(1, 5):
    print('----{}º PESSOA'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    soma += idade
    media = soma / 4
    if c == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > velho:
        velho = idade
        nomevelho = nome
if sexo in 'Ff' and idade < 20:
    cont += 1
print('A média de idades é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho    ))
print('Ao todo são {} mulheres abaixo de 20 anos'.format(cont))



