#coding: utf-8 
#------------------------------------------------------------------------------
#  Um programa que sorteia 5 números em uma lista usando uma função. E retorna
#  com uma outra função a soma de todos os números PARES gerados na lista.
#------------------------------------------------------------------------------
#  Funções para sortear e somar - Exercício #100
#------------------------------------------------------------------------------
from random import randint
from time import sleep

def sorteia(lista):
	print('\nSorteando 5 valores na lista:', end=' ')
	for c in range(5):
		lista.append(randint(1,10))
		print(c, end=' ', flush=True)
		sleep(0.5)
	print('PRONTO!')

def pares(lista):
	soma = 0
	for c in lista:
		if c % 2 == 0:
			soma += c
	print(f'Somando os valores pares de {lista}, temos o total de {soma}')
	print('\n> Fim Do Programa!')

numeros = []
sorteia(numeros)
pares(numeros)
print('---' *22)
