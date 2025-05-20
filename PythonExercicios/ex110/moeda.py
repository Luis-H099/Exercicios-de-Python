def metade(num, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def porcentagem(num, percent=10, formato=False):
    p = (num / 100) * percent
    res = num + p
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, baixo=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{porcentagem(preco, aumento, True)}')
    print(f'{baixo}% de redução: \t{diminuir(preco, baixo, True)}')
    print('-' * 30)