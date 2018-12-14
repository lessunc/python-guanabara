#coding: utf-8 
#----------------------------------------------
#  Um programa que recebe um número inteiro  
#  e retorna se esse é ou não um número primo.
#----------------------------------------------
#  Números Primos - Exercício #052
#----------------------------------------------
tot= 0
n = int(input('Digite um número para saber se ele é Primo: '))

for c in range(1, n +1):
	if n % c == 0:
		print('\033[1;35m', end='')#printa o número com cor
		tot+= 1
	else:
		print('\033[m', end='')#printa o número sem cor

	print(f'{c}', end=' ')

print('\033[m')
print(f'O número {n} foi divisível {tot} vezes..')

if tot== 2:
	print('Número Primo!\n')
else:
	print('Esse Número Não É Primo!\n')

