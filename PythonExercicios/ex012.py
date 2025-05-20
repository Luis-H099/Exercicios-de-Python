salario = float(input('Qual o salário do funcionário?'))
novo = salario + (salario * 5 / 100)
print('O reajuste do salário de R${} ficaria em R${}'.format(salario, novo))