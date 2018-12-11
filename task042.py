#coding: utf-8
#----------------------------------------------------------------------
#  Um programa que recebe o comprimento de 3 retas e retorna se essas
#  podem ou não formarem um triângulo, retornando ainda o tipo de 
#  triângulo que é formado apartir das medidas definidas.
#----------------------------------------------------------------------
#  Analizando um triângulo v2.0 - Exercício #042
#----------------------------------------------------------------------
n1 = int(input('Primeiro Seguimento: '))
n2 = int(input('Segundo Seguimento: '))
n3 = int(input('Terceiro Seguimento: '))

print('\033[31m===\033[m' * 22) #linha colorida(not important)

if n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n1 + n2:
	print('Os seguimentos formam um triâgulo' ,end=' ')

	if n1 == n2 == n3:
		print('EQUILÁTERO')

	elif n1 != n2 != n3 != n1:
		print('ESCALENO')

	else:
		print('ISÓSELES')		
else:
	print('Os seguimentos não formam triâgulo')

print('\033[31m===\033[m' * 22) #linha colorida(not important)

