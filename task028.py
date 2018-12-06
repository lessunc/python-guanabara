#coding: utf-8
#-----------------------------------------------------------------
#  Um programa que sorteia um numero de 1 a 5, recebendo um input
#  logo em seguida, e retornando se os números são iguais ou não. 
#-----------------------------------------------------------------
#  Jogo da adivinhação - Exercício #028
#----------------------------------------------------------------
from random import randint
from time import sleep

computador = randint(0,5)

print(f'\nVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[35m=-=\033[m' *22) #linha colorida(not important)

pessoa = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')
sleep(1)

if pessoa == computador:
	print('Parabéns! eu pensei nesse numero mesmo.')
	print('\033[35m>> you win <<\033[m')
else:
	print(f'Você errou! pensei no numero "{computador} e não no "{pessoa}"')
	print('\033[35m=-=\033[m' *22) #linha colorida(not important)

	