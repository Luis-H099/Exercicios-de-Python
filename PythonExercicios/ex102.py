def fatorial(num=1, show=True):
    '''
     -> Calcula o fatorial do número digitado.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    '''

    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == False:
        print('-' * 40)
        print(f)
    else:
        print(f'{num} ', end='')
        for c in range(num, 1, -1):
            print(f'x {c - 1} ', end='')
        print(f'= {f}')


fatorial(6, True)
help(fatorial)