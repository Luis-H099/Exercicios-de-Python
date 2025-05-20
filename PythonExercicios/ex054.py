contv = 0
contn = 0
for c in range(1,8):
    idade = int(input('Em que ano a {}º pessoa nasceu?: '.format(c)))
    if idade > 2006:
        contn += 1
    else:
        contn += 0
    if idade < 2007:
        contv += 1
    else:
        contv += 0
print('Ao todo tivemos {} pessoas maiores de idade'.format(contv))
print('Ao todo tivemos {} pessoas menores de idade'.format(contn))

