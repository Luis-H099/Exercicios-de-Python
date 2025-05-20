pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['idade'] = 2024 - pessoa['nascimento']
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + pessoa['contratação'] + 35 - 2024
print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k} tem valor de {v}')
