#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que contém uma função que recebe vários parâmetros com 
#  valores inteiros analizando os valores e retornando o maior deles.
#---------------------------------------------------------------------
#  Função que descobre o maior - Exercício #099
#---------------------------------------------------------------------
def linha():
	print('\033[2;35m=-=-\033[m' *11)

def conta(*n):
	linha()
	print(f'\033[35mAnalizando os valores passados...\033[m')
	for c in (n):
		print(c, end=' ')
	print(f'Foram informados {len(n)} valores ao todo.')
	print(f'O maior valor informado foi {max(n)}')

conta(2,3,1)
conta(5,6)
conta(3,2,2,4)
linha()

