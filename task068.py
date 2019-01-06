#coding: utf-8
#-------------------------------------------------------------------------
#  Um jogo de par ou ímpar que só é interrompido quando o jogador perder,
#  mostrando o total de vitórias consecutivas do jogador no final do jogo.
#-------------------------------------------------------------------------
#  Jogo do Par ou Ímpar - Exercício #068
#-------------------------------------------------------------------------
from random import randint
from time import sleep

v = 0
while True:

	player = int(input('Digite um Número: '))
	comp = randint(1,10)
	soma = player + comp
	opc = ' '

	while opc not in 'IP':
		opc = str(input('Par ou Ímpar: ')).strip().upper()[0]

	print('\033[1;35m___\033[m' *22) #linha colorida(not important)
	print('>>> IMPOU PAR \033[m<<< ') # ----------- (not important)
	print('\033[1;35m___\033[m' *22) #linha colorida(not important)
	sleep(1.5)

	print(f'Você Jogou {player} e o Computador {comp}.. Total: {soma}')
	sleep(1)

	if opc == 'P':
		if soma % 2 == 0:

			print('\033[35m>> Deu Par.. Você Venceu! <<\033[m',)
			sleep(2)
			v += 1

		else:
			print('\033[35m..Deu Ímpar! Você Perdeu.\033[m')
			break
	
	elif opc == 'I':
		if soma % 2 == 1:

			print('\033[35m>> Deu Ímpar.. Você Venceu! <<\033[m')
			sleep(2)
			v += 1

		else:
			print('\033[35m..Deu Par! Você Perdeu.\033[m')
			break

	print('\033[1;35m___\033[m' *22) #linha colorida(not important)
	print('..Vamos Jogar Novamente..')		
	
sleep(1)
print(f'\n>>> GAME OVER.. Você Venceu {v} vezes! <<<\n')

	

