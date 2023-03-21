print('{:=^40}'.format(' LOJAS MAXWEL '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    pagar = preço - (preço * 10 / 100)
elif opcao == 2:
    pagar = preço - (preço * 5 / 100)
elif opcao == 3:
    pagar = preço
    parcela = pagar / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    pagar = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = pagar / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalparc, parcela))
else:
    pagar = preço
    print('\033[31mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, pagar))
