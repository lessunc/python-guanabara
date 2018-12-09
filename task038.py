#coding: utf-8
#-------------------------------------------------------------------
#  Um programa que recebe e compara dois números inteiros e retorna
#  qual dos dois números é maior, ou se os dois números são iguais.
#-------------------------------------------------------------------
#  Comparando Números - Exercício #038
#-------------------------------------------------------------------

print('===' *22)
print('\033[31mSimples! Digite Dois Valores Para Saber Qual É Maior.\033[m')
print('===' *22)

pn = int(input('Primeiro Número: '))
sn = int(input('Segundo Número: '))

print('\033[31m')# código cor

if pn > sn:
	print('O Primeiro valor é maior')

elif sn > pn:
	print('O Segundo valor é maior')

else:
	print('Nenhum maior ...Os dois valores são iguais.')

print('\033[m')

