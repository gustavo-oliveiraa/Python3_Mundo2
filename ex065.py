opc = 'S'
totalnum = c = media = maior = menor = 0
while opc in 'Ss':
    num = int(input('Digite o {}º número: '.format(c+1)))
    totalnum += num
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opc = str(input('Deseja continuar a digitar valores? [S/N] ')).upper().strip()[0]
media = totalnum / c
print('\nVocê digitou {} números e a média foi {}'.format(c, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
