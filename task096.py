#coding: utf-8
#----------------------------------------------------------------------------
#  Um programa que recebe as dimensões de um terreno retangular (larg, comp)
#  em uma função, e retorna em seguida a área do terreno.
#----------------------------------------------------------------------------
#  Função que calcula área - Exercício #096
#----------------------------------------------------------------------------
print(f'\n{" CONTROLE DE TERRENOS ":-^48}')
def area(a, b):
	print(f'\nA área de um terreno de {a} x {b} é de {a * b} m²')

larg = float(input('> Largura: '))
comp = float(input('> Comprimento: '))

area(larg, comp)
print('---' *16)

