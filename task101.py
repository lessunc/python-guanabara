#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que contém uma função que recebe como parâmetro o ano de nascimento
#  de uma pessoa, retornando um valor literal indicando de acordo com sua idade se
#  essa pessoa tem o voto NEGADO, OPCIONAL, ou OBRIGATÓRIO no ano atual.
#---------------------------------------------------------------------------------
#  Funções para votação - Exercício #101
#---------------------------------------------------------------------------------
def voto(ano):
	from datetime import date
	n = date.today().year - ano

	if n < 16:
		return f'Com {n} anos: NÃO VOTA!\n'
	elif 16 <= n < 18 or n > 65:
		return f'Com {n} anos: VOTO OPCIONAL!\n'
	else:
		return f'Com {n} anos: VOTO OBRIGATÓRIO!\n'
print('---' *11)
print(voto(int(input('Ano de Nascimento: '))))

