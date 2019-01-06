#coding: utf-8
#------------------------------------------------------------------------
#  Um programa que recebe um número e retorna a tabuada desse, o progrma
#  continua pedindo os valores ao menos que o número seja negativo.
#------------------------------------------------------------------------
#  Tabuada v3.0 - Exercício #067
#------------------------------------------------------------------------
print('>> Digite Um Número Negativo Para Sair <<\n')

while True:
	tab = int(input('Quer ver a tabuada de qual número: '))
	print('\033[36m==\033[m' *22) #linha decorativa(not important)

	if tab < 0:
		break
	for c in range(1,11):
		print(f'{tab} x {c} = {tab * c}')

	print('\033[36m==\033[m' *22) #linha decorativa(not important)
print('Programa de tabuada encerrado. Volte Sempre!')

