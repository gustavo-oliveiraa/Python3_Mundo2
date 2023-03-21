#feito com while
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
#feito com for
'''num = int(input('Digite um número para calcular seu fatorial: '))
f = 1
c = num
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))'''
