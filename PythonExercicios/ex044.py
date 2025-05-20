print('-------------LOJINHA DE LUPROz-------------')
preco = float(input('Qual o preço da compra?: '))
forma = int(input(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/chegue
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a opção de pagamento? '''))
if forma == 1:
    valor = preco - (preco/100 * 10)
    print('o preço da sua compra será de R${}'.format(valor))
elif forma == 2:
    valor = preco - (preco / 100 * 5)
    print('o preço da sua compra será de R${}'.format(valor))
elif forma == 3:
    parcelas = preco / 2
    print('o preço da sua compra será de R${} e cada parcela estará saindo por R${}'.format(preco, parcelas))
elif forma == 4:
    n = int(input('Em quantas parcelas você estará fazendo?: '))
    valor = (preco / 100 * 20) + preco
    parcelas = valor / n
    print('''Sua compra será parcelada em {}x de R${} COM JUROS
    Sua compra de R${} vai custar R${} no final'''.format(n, parcelas, preco, valor))
else:
    print('Selecione uma opção válida!')



