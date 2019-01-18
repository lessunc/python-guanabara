#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que cria uma matriz recebendo valores até que essa seja preenchida.
#  O programa retorna a matriz formatada com os valores nas posições corretas, e:
#---------------------------------------------------------------------------------
#  • Soma dos valores pares.
#  • Soma dos valores da terceira coluna.
#  • O maior valor da segunda linha. 
#---------------------------------------------------------------------------------
#  Mais sobre Matriz em Python - Exercício #087
#---------------------------------------------------------------------------------
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somap = somaI = ter = 0

for m in range(0,3):
	for c in range(0,3):
		matriz[m][c] = int(input(f'Digite um valor na posição [{m},{c}]: '))
		if c == 2:
			ter += matriz[m][c]

		if matriz[m][c] % 2 == 0:
			somap += matriz[m][c]
		else:
			somaI += matriz[m][c]

print('\n{:~^36}'.format('\033[35mMATRIZ\033[m'))#linha decorativa(not important)
for m in range(0,3):
	for c in range(0,3):
		print(f'(\033[35m{matriz[m][c]:^5}\033[m)', end= ' ')
	print()

print('~~' *14)
print(f'\nSoma dos valores pares= {somap}')
print(f'Soma dos números ímpares= {somaI}')
print(f'Soma dos números da 3ª coluna= {ter}')
print(f'Maior valor da 2ª coluna= {max(matriz[1])}\n')

