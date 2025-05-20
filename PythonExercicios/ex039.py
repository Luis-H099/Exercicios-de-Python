data = int(input('Qual seu ano de nascimento: '))
anos = 2024 - data
alistamento = data + 18
final = alistamento - 2024
print('Quem nasceu em {} tem {} anos em 2024'.format(data, anos))
if anos > 18:
    saldo = anos - 18
    print('Você já deveria ter se alistado há {} anos atrás'.format(saldo))
    print('Seu alistamento foi em {}'.format(alistamento))
elif anos < 18:
    print('Você irá se alistar daqui {} anos'.format(final))
    print('O ano do seu alistamento será em {}'.format(alistamento))
else:
    print('Você deve se alistar URGENTEMENTE!')

