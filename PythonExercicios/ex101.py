def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {ano} anos: NÃO VOTA!'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {ano} anos: VOTO OPCIONAL!'
    else:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))