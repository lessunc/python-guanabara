#coding: utf-8
#-----------------------------------------------------------
#  Um programa que calcula a soma entre os números ímpares 
#  que são múltiplos de três entre um intervalo de 1 a 500
#-----------------------------------------------------------
#  Soma de ímpares múltiplos de três - Exercício #048
#-----------------------------------------------------------
from time import sleep

soma = 0
cont = 0

for c in range(1, 501, 2):
	if c % 3 == 0:
		soma = soma + c
	cont += 1

print('\n..Calculando a soma de ímpares múltiplos de 3 entre 1 à 500')
sleep(3)	
print(f'A soma de todos os {cont} valores solicitados é: {soma}')

