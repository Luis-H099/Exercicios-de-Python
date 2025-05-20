def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def porcentagem(num, percent=10):
    p = (num / 100) * percent
    return num + p


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')