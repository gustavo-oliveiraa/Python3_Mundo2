frase = str(input('Digite uma frase: ')).strip().upper() # eliminei os epaços antes e depois com strip
palavras = frase.split()
junto = ''.join(palavras) # e eliminei os espaços internos, com os comandos split e join
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
