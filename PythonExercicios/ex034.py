s = float(input('Qual o salário do funcionário? R$'))
if s < 1250:
    novo = (s / 100) * 115
else:
    novo = (s / 100) * 110
print('O salário antigo de R${:.2f}, agora será de R${:.2f}!'.format(s, novo))
