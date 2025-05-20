from random import randint
print('-=-' * 20)
print('Irei escolher um número entre 0 e 3, você consegue adivinhar?')
print('-=-' * 20)
escolhido = randint(0,3)
num = int(input('Tente adivinhar o número que a máquina está pensando: '))
print('-=-' * 10 , "PROCESSANDO...",  '-=-' * 10)
if num == escolhido:
    print('Você acertou o número, PARABÉNS!')
else:
    print('Você infelizmente errou, eu pensei no número {} e você no {}, tente novamente!'.format(escolhido, num))
print('==============FIM DE JOGO================')