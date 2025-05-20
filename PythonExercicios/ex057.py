s = ''
s = str(input('Informe seu sexo[F/M]: '.upper()))
while s not in 'MmFfs':
    s = str(input('Dados incorretos, informe seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))
