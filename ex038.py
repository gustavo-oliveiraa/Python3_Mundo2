num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O {}PRIMEIRO valor{} é {}maior{}.'.format('\033[31m', '\033[m', '\033[34m', '\033[m'))
elif num2 > num1:
    print('O {}SEGUNDO valor{} é {}maior{}.'.format('\033[31m', '\033[m', '\033[34m', '\033[m'))
else:
    print('{}Não existe{} valor maior, os dois são {}IGUAIS{}.'.format('\033[31m', '\033[m', '\033[34m', '\033[m'))
