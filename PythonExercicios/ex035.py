a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('Os três segmentos PODEM formar um triângulo')
else:
    print('Os três segmentos NÃO PODEM formar um triângulo')
