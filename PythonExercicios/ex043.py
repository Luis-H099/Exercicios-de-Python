kg = float(input('Qual seu peso? (kg): '))
altura = float(input('Qual sua altura? (m): '))
IMC = kg / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal. SE CUIDE!')
elif 18.5 <= IMC < 25:
    print('Parabéns, você está na faixa de PESO NORMAL')
elif 25 <= IMC < 30:
    print('Você está na faixa de SOBREPESO! Fique atento!')
elif 30 <= IMC < 40:
    print('Você está na faixa de OBESIDADE!')
elif IMC >= 40:
    print('Você está na faixa de OBESIDADE MÓRBIDA! Cuidado!')
