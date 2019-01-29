#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que contém uma função que recebe dois parâmetros opcionais sendo 
#  eles o nome do jogador e quantos gols ele marcou. O programa deve mostrar a 
#  ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
#---------------------------------------------------------------------------------
#  Ficha do Jogador - Exercício #103
#---------------------------------------------------------------------------------
def ficha(a='<desconhecido>',b=0):
	
	print(f'\nO jogador {a} fez {b} gol(s) no campeonato.')
	print('---' *22)
jog = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))

if gols.isnumeric():
	gols = int(gols)
else:
	gols = 0
if jog.strip() == '':
	ficha(b=gols)
else: 
	ficha(jog,gols)
