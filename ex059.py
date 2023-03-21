from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do Programa')
    opc = int(input('Qual é sua opção? '))
    if opc == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))
        print('=-=' * 10)
        print('Voltando ao menu...')
        sleep(4)
    elif opc == 2:
        produto = num1 * num2
        print('O produto entre {} x {} é {}'.format(num1, num2, produto))
        print('=-=' * 10)
        print('Voltando ao menu...')
        sleep(4)
    elif opc == 3:
        if num1 > num2:
            maior = num1
            print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
            print('=-=' * 10)
            print('Voltando ao menu...')
            sleep(4)
        elif num2 > num1:
            maior = num2
            print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
            print('=-=' * 10)
            print('Voltando ao menu...')
            sleep(4)
        else:
            print('Entre {} e {} não tem maior valor pois são iguais.'.format(num1, num2))
            print('=-=' * 10)
            print('Voltando ao menu...')
            sleep(4)
    elif opc == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('=-=' * 10)
        print('Voltando ao menu...')
        sleep(4)
    elif opc == 5:
        print('Finalizando...')
        print('=-=' * 10)
        sleep(4)
        print('Fim do program! Volte sempre!')
    else:
        print('\033[31mOpção inválida tente novamente.\033[m')
        print('=-=' * 10)
        print('Voltando ao menu...')
        sleep(4)
