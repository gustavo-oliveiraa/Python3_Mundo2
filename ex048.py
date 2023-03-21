soma = 0  # acumulador --> acumulando os valores
cont = 0  # contador --> conta mais 1
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

#cont = cont + 1
