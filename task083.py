#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que recebe uma expressão com parênteses, analizando se a expressão
#  está com parênteses abertos e fechados corretamente, identificando por pares.
#---------------------------------------------------------------------------------
#  Validando expressões matemáticas - Exercício #083
#---------------------------------------------------------------------------------
expr = str(input('digite uma expressão: '))
cont = []

for e in expr:
	if e == '(':
		cont.append('(')

	elif e == ')':
		if len(cont) > 0:
			cont.pop()

		else:
			cont.append(')')
			break

print('\033[1;35m~~\033[m' *22)# linha decorativa(not important)

print(f'Sua Expressão: {expr}')

if len(cont) == 0:
	print('\033[35mEssa Expressão Está Correta!')

else: 
	print('\033[35mEssa Expressão Está Incorreta!\033[m')
	print(f'Caracteres excedentes: {cont}')

print('\033[1;35m~~\033[m' *22)# linha decorativa(not important)

