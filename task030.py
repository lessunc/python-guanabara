#coding: utf-8
#------------------------------------------------------
#  Um programa que recebe um número inteiro e retorna 
#  se esse é par ou ímpar
#------------------------------------------------------
#  Par ou Ímpar - Exercício #030
#------------------------------------------------------

n = int(input('Digite um número para saber se é par ou impar: '))
result = n % 2 

if n % 2 == 0:
	print('\033[45m >> PAR << \033[m')

elif n % 2 == 1:
	print('\033[45m >> IMPAR << \033[m')

