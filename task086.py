#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que cria uma matriz recebendo valores até que essa seja preenchida.
#  O programa retorna a matriz formatada com os valores nas posições corretas.
#---------------------------------------------------------------------------------
#  Matriz em Python - Exercício #086
#---------------------------------------------------------------------------------
li = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for cont in range(0,3):
	for c in range(0,3):
		li[cont][c] = int(input(f'Digite um valor para a posição [{cont}, {c}]: '))
print('\n{:…^38}'.format('MATRIZ'))# linha decorativa(not important)

for cont in range(0,3):
	for c in range(0,3):
		print(f'   [{li[cont][c]:^5}]',end=' ')
	print()
print('……' *19)

