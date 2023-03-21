nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno está \033[31mREPROVADO!')
elif 5 <= media < 7:
    print('O aluno está em \033[34mRECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está \033[32mAPROVADO!')

#elif media >= 7.0 and media <= 10.0:
#elif 5 <= media < 7: --> PODE SER FEITO DOS DOIS JEITOS.
