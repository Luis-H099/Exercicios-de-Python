jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]  ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')