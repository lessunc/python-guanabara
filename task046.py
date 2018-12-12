#coding: utf-8
#-----------------------------------------------------------
#  Um programa que mostra na tela uma contagem regressiva  
#  de 10 à 0 com uma pausa de meio segundo entre eles.
#-----------------------------------------------------------
#  Contagem Regressiva- Exercício #046
#-----------------------------------------------------------
from time import sleep
print('\033[33mContagem Regressiva Para Os Fogos\033[m...')

for c in range(10, -1, -1):
	print(c)
	sleep(0.5)

print('\033[33mBOOM POOM POW !!!\033[m')
print('**' *11)

