def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyBoardInterrupt:
            print('\033[31mERRO: O usuário decidiu não informar esse valor.\033[m')
            return 0
        else:
            return i

def leiafloat(msg):
    while True:
        try:
            i = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número real válido.\033[m')
            continue
        except KeyBoardInterrupt:
            print('\033[31mERRO: O usuário decidiu não informar esse valor.\033[m')
            return 0
        else:
            return i


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real {n2}')

