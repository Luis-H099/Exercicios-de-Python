valor = int(input('Qual o valor da casa? '))
salario = int(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
financiamento = valor/(anos * 12)
final = 30 * (salario/100)
print('Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}'.format(valor, anos, financiamento))
if final > financiamento:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO')