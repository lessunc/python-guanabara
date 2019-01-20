#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que simula 4 jogadores jogando um dado, gerando 
#  valores aleatórios e guardando esses em um dicionário e em ordem, 
#  sabendo que que o vencedor é o jogador com o maior número gerado.
#---------------------------------------------------------------------
#  Jogo de Dados em Python - Exercício #091
#---------------------------------------------------------------------
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
		'jogador2': randint(1,6),
		'jogador3': randint(1,6),
		'jogador4': randint(1,6)}

ranking = []
print('\033[36m>>> VALORES SORTEADOS <<<\033[m')
for k, v in jogo.items():
	print(f'{k} jogou {v} no dado.')
	sleep(1)

print('\n\033[36m>>> RANKING DOS JOGADORES <<<\033[m')
ranking = sorted(jogo.items(), key= itemgetter(1), reverse= True)
for e, c in enumerate(ranking):
	print(f'  • {e +1}º lugar: {c[0]} com {c[1]}')
print()
