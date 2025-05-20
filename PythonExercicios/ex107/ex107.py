from ex107.uteis107 import metade, dobro, porcentagem
valor = int(input('Digite um preço: R$'))
print(f'A metade de R${valor} é R${metade(valor)}')
print(f'O dobro de R${valor} é R${dobro(valor)}')
print(f'Aumentando 10% temos R${porcentagem(valor, 10)}')