jogador = dict()
partidas = list()
jogador['nome'] = str(input('Qual o nome do jogador: '))
tot = int(input(f'Quantas partidas o jogador {jogador['nome']} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {tot} partidas.')
for c in range(0,tot):
    print(f'=> Na partida {c}, ele fez {jogador['Gols'][c]} gols')
print(f'Foi um total de {jogador['Total']}')
