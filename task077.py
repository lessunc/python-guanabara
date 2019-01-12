#coding: utf-8
#--------------------------------------------------
#  Um programa que mostra todas vogais de cada
#  palavra contida em uma tupla única já definida.
#--------------------------------------------------
#  Contando vogais em Tuplas - Exercício #077
#--------------------------------------------------
from time import sleep
print('\033[36m====\033[m' *11)# linha decorativa(not important)

coisas = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'pratica')
for c in coisas:
	print(f'Na palavra {c.upper()} temos as vogais', end=' ')

	for letra in c:
		if letra in 'aeiou':
			print(f'{letra.upper()}', end=' ')	
	print()
	sleep(0.7)
print('\033[36m====\033[m' *11)# linha decorativa(not important)
	
