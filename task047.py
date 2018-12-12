#coding: utf-8
#-----------------------------------------------
#  Um programa que mostra na tela uma contagem 
#  de 0 à 50 com apenas números pares.
#-----------------------------------------------
#  Contagem de pares - Exercício #047
#-----------------------------------------------
from time import sleep

#printa de 1 a 50 apenas numeros pares
for c in range(1, 52):
	if c % 2 == 0:
		print(c, end=' ', flush=True)
		sleep(0.1)
print('ACABOU !')

