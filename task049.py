#coding: utf-8
#-----------------------------------------------
#  Um programa que recebe um número inteiro e 
#  retorna sua tabuada utilizando o laço for.
#-----------------------------------------------
#  Tabuada v2.0 - Exercício #049
#-----------------------------------------------

n = int(input('Digite um valor para visualizar a sua tabuada: '))

for c in range(1, 10):
	conta = n * c
	print (f'{n} x {c} = {conta}')

