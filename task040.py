#coding: utf-8
#-----------------------------------------------------------------
#  Um programa que recebe duas notas de um aluno calcula a média 
#  retornando ainda se o aluno está reprovado, em recuperação, ou
#  aprovado de acordo com a média calculada.
#-----------------------------------------------------------------
#  Aquele clássico da média - Exercício #040
#-----------------------------------------------------------------

nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2

print('\033[35m---\033[m' * 22) #linha colorida(not important)
print(f'Tirando "{nota1}" e "{nota2}", sua média é de: "{media}"\033[m')

if media < 5.0:
	print('Abaixo da média ...o aluno está \033[35mREPROVADO!\033[m')

elif 7.0 > media >= 5.0:
	print('O aluno está em \033[35mRECUPERAÇÃO!\033[m')

else:
	print('O aluno está \033[35mAPROVADO!\033[m')

print('\033[35m---\033[m' * 22) #linha colorida(not important)

