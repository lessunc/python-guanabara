#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que contém uma função que recebe dois parâmetros sendo o primeiro
#  o número a ser calculado, e o outro sendo um valor lógico(opcional) que indica
#  se o processo do cálculo da fatororial será exibido ou não. Incluso docstring.
#---------------------------------------------------------------------------------
#  Função para Fatorial - Exercício #102
#---------------------------------------------------------------------------------
print('\n-- FATORIAL DE 5 --')
def fatorial(n=1, show=False):
	"""
	=> Calcula o Fatorial de um número.
	:parâmetro n: O número a ser calculado.
	:parâmetro show: (opcional) Mostrar ou não a conta.
	:return: O valor do Fatorial de um número n.
	"""
	f = 1
	for c in range(n, 0, -1):
		if show == True:
			print(c, end = ' ')
			if c > 1:
				print('x', end =' ')
			if c == 1:
				print('=', end =' ')
		f *= c
	return f
print(fatorial(5, True))
