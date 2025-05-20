print('='*20)
print('    10 TERMOS DE UMA PA')
print('='*20)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
f = r * 10
for c in range(p1, f, r):
    print('{} ➺'.format(c), end=' ')
print('ACABOU!')
