#coding: utf-8
#-------------------------------------------------------------------------
#  Aprimoramento do Exercício 093. Programa que gerencia o desempenho de 
#  vários jogadores de futebol, recebendo e armazenando em um dicionário:
#-------------------------------------------------------------------------
#  • O nome do jogador| • Quantas partidas foram jogadas|  
#  • Quantos gols foram feitos em cada partida| • Total de gols.
#-------------------------------------------------------------------------
#  Aprimorando os dicionários - Exercício #095
#-------------------------------------------------------------------------
from time import sleep
time = []
while True:
	jogo = []
	dic = {}
	dic['jogador'] = str(input('Nome do jogador: ')).capitalize()
	partidas = int(input(f'Quantas partidas {dic["jogador"]} jogou? '))
	
	for c in range(partidas):
		jogo.append(int(input(f'  • Quantos gols {dic["jogador"]} fez na {c+1}ª partida? ')))
		dic['gols'] = jogo[:]
		dic['total'] = sum(jogo)
	time.append(dic)
	while True:
		opc = str(input('\n\033[36mQuer continuar? [s/n]:\033[m'))
		if opc in 'sn':
			break
		print('ERRO NA DIGITAÇÃO!')
	if opc == 'n':
		break

#tabela geral de jogadores/partidas/gols 			
print('\033[36m___\033[m' *22)
print(f'{"Cod.":<3} {"JOGADOR":<15} {"GOLS":<15} {"TOTAL":<15}'	)
print('\033[36m___\033[m' *22)

for e, c in enumerate(time):
	print(f'{e+1:<3}',end=' ')
	print(f'{c["jogador"]:<15} {str(c["gols"]):<15} {c["total"]:<15}')

#dados individuais do jogador
while True:
	busca = int(input('\n\033[36mMostrar dados de qual jogador? (999 para parar)\033[m'))
	busca -= 1
	if busca == 998:
		break
	if busca >= len(time) or busca < 0:
		print('ERRO!   ..Não existe jogador com esse código.')
	else:
		print('\033[36m___' *22)
		print(f'LEVANTAMENTO DE DADOS DO JOGADOR {time[busca]["jogador"].upper()}\033[m')
		sleep(2.3)

		for e, c in enumerate(time[busca]["gols"]):
			print(f'No {e+1}º jogo fez {c} gols.')
sleep(0.5)
print('> FINALIZADO.\n')

