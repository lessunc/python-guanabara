#coding: utf-8
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