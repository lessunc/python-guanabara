#coding: utf-8 
#---------------------------------------------------------------------
#  Um programa que gerencia o desempenho de um jogador de futebol.
#  O programa deve ler e armazenar em um dicionário :
#  • O nome do jogador| • Quantas partidas foram jogadas|  
#  • Quantos gols foram feitos em cada partida| • Total de gols.
#---------------------------------------------------------------------
#  Cadastro de Jogador de Futebol - Exercício #093
#---------------------------------------------------------------------
dic = {}
jogo = []
dic['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dic["jogador"]} jogou? '))
for c in range(partidas):
	jogo.append(int(input(f'   • Quantos gols {dic["jogador"]} fez na {c+1}ª partida? ')))
	dic['gols'] = jogo[:]
	dic['total'] = sum(jogo)

#primeira opção(formatação do print) 
print('___' *22) 
print(f' {dic} ')
print('___' *22) 

#segunda opção(formatação do print) 
for k, v in dic.items():
	print(f'{k} --- {v}')

#terceira opção(formatação do print)
print('___' *22)
print(f'O jogador {dic["jogador"]} jogou {len(dic["gols"])} partidas.')
for e, j in enumerate(dic['gols']):
	print(f'   => Na partida {e+1} fez {j} gols.')

print(f'\nfoi um total de {dic["total"]} gols!!!')
print('___' *22)

	