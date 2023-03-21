print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA P.A'))
print('='*40)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU', end=' ')

#print('{:=^40}'.format(' LOJAS MAXWEL '))
