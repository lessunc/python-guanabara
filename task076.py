#coding: utf-8
#----------------------------------------------------------------
#  Um programa que organiza nomes de produtos e seus respectivos
#  preços de uma tupla única em uma listagem de forma tabular.
#----------------------------------------------------------------
#  Lista de preços com Tupla - Exercício #076
#----------------------------------------------------------------
#cabeçalho decorativo(not importat)
print('\033[35m____\033[m' *11)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('\033[35m____\033[m' *11)

tupla = ('queijo', 5.50, 'pãozinho', 2.00, 'bolo', 34.00, 'pudim', 3.00)

for c in tupla:
	if tupla.index(c) % 2 == 0:
		print(f'{c:.<30}', end=' ')
	else:
		print(f'R$ {c:>6.2f}')
print('\033[35m____\033[m' *11)# linha decorativa(not important)

