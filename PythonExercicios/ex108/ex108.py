from ex107 import uteis107

valor = float(input('Digite um preço: R$'))
print(f'A metade de {uteis107.moeda(valor)} é {uteis107.moeda(uteis107.metade(valor))}')
print(f'O dobro de {uteis107.moeda(valor)} é {uteis107.moeda(uteis107.dobro(valor))}')
print(f'Aumentando 10% temos {uteis107.moeda(uteis107.porcentagem(valor, 10))}')