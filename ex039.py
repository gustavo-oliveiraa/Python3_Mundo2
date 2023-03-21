from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(falta))
    ano = atual + falta
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    passou = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(passou))
    ano = atual - passou
    print('Seu alistamento foi em {}.'.format(ano))

#from datetime import date
#atual = date.today().year
