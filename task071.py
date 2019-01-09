#coding: utf-8
#----------------------------------------------------------------------------
#  Um programa que recebe o valor a ser sacado simulando um caixa eletrônico, 
#  retornando quantas cédulas e de qual valor serão entregues, considerando 
#  que o caixa possui apenas cédulas de R$50 | R$20 | R$10 | R$1  
#----------------------------------------------------------------------------
#  Simulador de Caixa Eletrônico - Exercício #071
#----------------------------------------------------------------------------
from time import sleep

#cabeçalho decorativo(not important)
print('\033[35m=-=\033[m' * 11)
print('{:^30}'.format('-- Banco Naumideva --'))
print('\033[35m=-=\033[m' * 11)

saque = int(input('Quanto Deseja Sacar? '))
total = saque
nota = 50
limite = 0

while True:
	if total >= nota:
		total -= nota
		limite += 1
	else:
		if limite > 0:
			sleep(1)
			print(f'\n\033[35m{limite} notas de R${nota},00\033[m')

		if nota == 50:
			nota = 20
		elif nota == 20:
			nota = 10
		elif nota == 10:
			nota = 5
		elif nota == 5:
			nota = 1
		limite = 0
		if total == 0:
			break

print('\033[35m___\033[m' *22) #linha decorativa(not important)
print('Obrigado Por Usar o Banco Naumideva. Volte Sempre!  :)')
print('\033[35m___\033[m' *22) #linha decorativa(not important)

