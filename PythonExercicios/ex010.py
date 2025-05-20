l = float(input('Qual a largura da parede?'))
al = float(input('Qual a altura da parede?'))
a = l * al
t = a / 2
print('A sua parede tem dimensões de {}x{} e uma área de {}m².\n para pintar essa parede você precisara de {}L de tinta.'.format(l, al, a, t))