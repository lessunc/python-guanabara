#coding: utf-8
#---------------------------------------------------------------
#  Um programa que recebe 6 números inteiros e retorna a soma 
#  de todos os números pares desconsiderando os números ímpares.
#---------------------------------------------------------------
#  Soma dos pares - Exercício #051
#---------------------------------------------------------------

print('\033[2;34m=-=-\033[m' *11) #linha colorida(not important) 
print('10 Termos De Uma P.A')
print('\033[2;34m=-=-\033[m' *11) #linha colorida(not important) 

pri = int(input('Primeiro Termo: '))
rz = int(input('Razão: '))

print()
for c in range(pri, pri + (10 * rz), rz):
	print(c, end = '-> ')

print('ACABOU !')

