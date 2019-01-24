#coding: utf-8
#----------------------------------------------------------------------------
#  Um programa que recebe as dimensões de um terreno retangular (larg, comp)
#  em uma função, e retorna em seguida a área do terreno.
#----------------------------------------------------------------------------
#  Função que calcula área - Exercício #096
#----------------------------------------------------------------------------
print(f'\n{" controle de terrenos ":-^48}'.upper())

def area(a, b):
	print(f'A area de um terreno de {a} x {b} é de {a * b} m²')
	
larg = float(input('\033[35m> Largura: '))
comp = float(input('> Comprimento: '))
print('\033[m')

area(larg, comp)
print('---' *16)

