speed = int(input('Qual a velocidade atual do carro? '))
if speed > 80:
    print('Você foi multado por exceder o limite de velocidade que é 80km/h')
    multa = (speed-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia, Dirija com segurança!')
90
