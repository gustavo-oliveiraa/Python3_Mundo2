sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # [0] é para pegar somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
