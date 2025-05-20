dados = dict()
nome = str(input('Nome: '))
media = float(input(f'Média do aluno {nome}: '))
dados['Nome'] = nome
dados ['Media'] = media
print('-=' * 30)
if media >= 7:
    dados['situação'] = 'Aprovado'
elif 6 < media < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
for k, v in dados.items():
    print(f' -- {k} é igual a {v}')