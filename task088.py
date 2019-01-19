#coding: utf-8
#------------------------------------------------------------------------
#  Um programa que recebe um número N, e gera N listas sorteadas com
#  seis números entre 1 e 60, cadastrando tudo em uma lista composta.
#  O programa identifica e não adiciociona números repetidos nas listas.
#------------------------------------------------------------------------
#  Palpites para a Mega Sena - Exercício #088
#------------------------------------------------------------------------
from random import randint
from time import sleep
#decorativo(not important)
print('\033[35m---\033[m' * 14)
print('{:^38}'.format(' JOGO DA MEGA SENA '))
print('\033[35m---\033[m' * 14)

dados = []
jogos = []
qtd = int(input('Quantos Jogos Vamos Sortear: '))
print('\n{:^36}'.format(f' SORTEANDO {qtd} JOGOS '))

print('\033[35m---\033[m' * 14)# linha decorativa(not important)
for c in range(0, qtd):	
	for q in range(0,6):
		n = randint(0,60)
		while n in jogos:
			n = randint(0,60)
		jogos.append(n)
	jogos.sort()
	sleep(0.5)

	print(f'\033[35mJOGO {c+1}: \033[m{jogos}')
	dados.append(jogos[:])
	jogos.clear()
print('\033[35m---\033[m' * 14)# linha decorativa(not important)

