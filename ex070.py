total = totmil = cont = menor = 0
menorNome = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        menorNome = produto
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorNome} que custa R${menor:.2f}')
