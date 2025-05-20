a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
media = (a + b) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(a, b , media))
if media >= 7:
    print('O aluno está APROVADO!')
elif media < 5:
    print('O aluno está REPROVADO!')
else:
    print('O aluno está de RECUPERAÇÃO')
