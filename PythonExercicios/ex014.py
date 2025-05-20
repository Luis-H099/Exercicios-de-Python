dias = int(input('Por quantos dias foram usado o carro?     '))
km = float(input('Quantos Km foram rodados com o carro? '))
pago = (dias * 60) + (km * 0.15)
print('O preço do carro alugado será {:2f}'.format(pago))