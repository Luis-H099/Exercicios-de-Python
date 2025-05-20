from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
ano = atual - nasc
print('O atleta tem {} anos'.format(ano))
if ano < 10:
    print('Classificação: MIRIM')
elif ano > 9 and ano < 15:
    print('Classificação: INFANTIL')
elif ano > 14 and ano < 20:
    print('Classificação: JUNIOR')
elif ano > 19 and ano < 26:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')