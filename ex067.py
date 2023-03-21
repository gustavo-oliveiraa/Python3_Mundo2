while True:
    num = int(input('Qual valor deseja ver a tabuada? (Use um número negativo para parar) '))
    print('-'*30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {cont * num}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

'''
while cont <= 10:
    print(f'{num} x {cont:2} = {cont * num}')
    cont += 1
    cont = 1
'''