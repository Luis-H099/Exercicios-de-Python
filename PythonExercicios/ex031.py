distance = float(input('Qual a distância da viagem? '))
print('Você iniciará uma viagem de {}Km.'.format(distance))
if distance <= 200:
    preço = distance * 0.5
else:
    preço = distance * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preço))
