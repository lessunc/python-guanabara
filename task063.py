#coding: utf-8
#----------------------------------------------------------
#  Um programa que recebe um número n inteiro, e retorna 
#  os n primeiros elementos de uma Sequência de Fibonacci.
#----------------------------------------------------------
#  Sequência de Fibonacci v1.0 - Exercício #063
#----------------------------------------------------------

print('\033[35m>> FREQUÊNCIA DE FIBONACCI <<\033[m\n')

termo = int(input('Quantos termos você quer mostrar na sequencia: '))
pt = 0
st = 1
loop = 3
soma = 0

print('\033[35m===\033[m' *22) #linha colorida(not important)

print(f'{pt} -> {st} ->',end='')
while loop <= termo:

	soma = pt + st
	print(f'{soma} ->',end=' ')

	pt = st
	st = soma
	loop += 1

print('FIM!')
print('\033[35m===\033[m' *22) #linha colorida(not important)

