#coding: utf-8
#----------------------------------------------------------------------------------
#  Um programa que recebe e cadastra sete números em uma lista única separando os
#  valores pares e ímpares em listas internas, retornando esses em ordem crescente.
#----------------------------------------------------------------------------------
#  Lista com pares e ímpares - Exercício #085
#----------------------------------------------------------------------------------
li = [[],[]]

for c in range(1,8):
	n = (int(input(f'Digite o {c}º valor: ')))
	li[n % 2].append(n)

print(f'\nOs valores pares foram {sorted(li[0])}') 
print(f'Os valores ímpares foram {sorted(li[1])}')
print('\033[36m...\033[m' * 16)#linha decorativa(not important)

