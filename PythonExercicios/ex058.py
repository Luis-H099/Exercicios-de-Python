from random import randint
computador = randint(0,10)
print('Sou seu computador... acabei de pensar em um número de 0 a 10,')
print('quantas tentativas você precisará para acertar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente outra vez')
        else:
            print('Mais... Tente outra vez')
print('Acertou!')
print('Você acertou em {} tentativas'.format(palpite))