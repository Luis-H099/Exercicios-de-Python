from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
escolha = int(input('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura
Qual sua escolha?: '''))
print('-=' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[escolha]))
print('-=' * 11)
if computador == 0:
    if escolha == 0:
        print('O jogo deu EMPATE!')
    elif escolha == 1:
        print('O jogador VENCEU!')
    elif escolha == 2:
        print('O jogador PERDEU!')
elif computador == 1:
    if escolha == 1:
        print('O jogo deu EMPATE!')
    elif escolha == 2:
        print('O jogador VENCEU!')
    elif escolha == 0:
        print('O jogador PERDEU!')
elif computador == 2:
    if escolha == 2:
        print('O jogo deu EMPATE!')
    elif escolha == 0:
        print('O jogador VENCEU!')
    elif escolha == 1:
        print('O jogador PERDEU!')