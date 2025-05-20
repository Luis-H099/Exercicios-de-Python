primeiro = int(input('Qual é o primeiro valor: '))
segundo = int(input('Qual é o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''   [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>> Qual sua opção? '))
    if opcao == 1:
        resultado = primeiro + segundo
        print('A soma entre os dois números é {}'.format(resultado))
    elif opcao == 2:
        resultado = primeiro * segundo
        print('A multiplicação entre os dois números é de {}'.format(resultado))
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('Entre {} e {} o maior valor é o {}'.format(primeiro, segundo, maior))
    elif opcao == 4:
        print('Digite os números novamente!')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif  opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inváilida, Digite novamente')
    print('-=' * 20)
print('Fim do programa. Volte sempre!')

