from datetime import date
atual = date.today().year
idades = {}
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Ano de nascimento da {}ª pessoa:'.format(c+1)))
    idade = atual - ano
    idades[c] = idade
for c in range(0, 7):
    if idades[c] < 21:
        print('A {}ª pessoa tem {} anos e é menor de idade.'.format(c+1, idades[c]))
        menor += 1
    else:
        print('A {}ª pessoa tem {} anos e é maior de idade.'.format(c+1, idades[c]))
        maior += 1
print('\nAo todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E tivemos {} pessoas menores de idade.'.format(menor))
