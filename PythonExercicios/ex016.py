from math import hypot
cat1 = float(input('Digite o valor do cateto oposto:'))
cat2 = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(cat1, cat2)
print('A hipotenusa vai medir {:.2f}'.format(hi))