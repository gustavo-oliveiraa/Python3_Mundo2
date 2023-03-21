num = cont = soma = 0
print('Digite quantos números quiser somar, para parar é so digitar 999.')
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        print('Saindo obrigado, por usar este programa.')
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
