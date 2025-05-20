def ficha(nome='', gols=0):
    if nome in '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
n = str(input('Digite o nome do jogador: '))
g = str(input(f'Informe o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)