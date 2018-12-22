#coding: utf-8
#----------------------------------------------------------
#  Um programa que recebe um número n inteiro, e retorna 
#  os n primeiros elementos de uma Sequência de Fibonacci.
#----------------------------------------------------------
#  Sequência de Fibonacci v1.0 - Exercício #063
#----------------------------------------------------------
from time import sleep

print('\033[2;35m>> FREQUÊNCIA DE FIBONACCI <<\033[m\n')
termo = int(input('Quantos termos você quer mostrar na sequencia: '))
pt = 0
st = 1
loop = 3
soma = 0

print('\033[2;35m') #cor
print(f'{pt} -> {st} -> ',end='', flush = True)
sleep(0.1)

while loop <= termo:
	soma = pt + st
	print(f'{soma} -> ',end='', flush = True)
	pt = st
	st = soma
	loop += 1
	sleep(0.1)

print('FIM!\033[m')

