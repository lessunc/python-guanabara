#coding: utf-8
#---------------------------------------
#  Um programa que recebe um número 
#  qualquer e retorna seu fatorial.
#---------------------------------------
#  Cálculo do Fatorial - Exercício #060
#---------------------------------------
fatorial = 1

n = int(input('Digite um valor para saber seu fatorial:'))

print(f'..CALCULANDO FATORIAL DE {n}!')
print('\033[2;36m...\033[m' * 22)#linha colorida(not important)

for c in range(n, 0, -1):
	fatorial *= c
	
	print(c, end='')
	print(' x ' if c > 1 else ' = ',end='')

print(f'{fatorial}')
print('\033[2;36m...\033[m' * 22) #linha colorida(not important)
	