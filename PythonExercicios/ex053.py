frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a palavra {}'.format(junto))
for letras in range(len(junto) -1,-1,-1):
    inverso += junto[letras]
print('Esta frase invertida se escreve {}'.format(inverso))
if inverso == junto:
    print('Opa! Achamos um PALÍNDROMO')
else:
    print('Sua frase infelizmente não é um PALÍNDROMO')
