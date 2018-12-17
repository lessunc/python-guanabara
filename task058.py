#coding: utf-8
#-----------------------------------------------------------------
#  Um jogo em que o programa escolhe um número entre 0 e 10.
#  Pedindo em seguida que o jogador adivinhe qual foi, recebendo
#  valores até que esse seja igual ao escolhido pelo programa, e 
#  retornando quantas partidas foram necessárias para adivinhar.
#------------------------------------------------------------------
#  Jogo da Adivinhação v2.0 - Exercício #058
#------------------------------------------------------------------
from random import randint

tentativas = 1

print('\033[1;35mSou seu computador...\033[m')
print('Acabei de pensar em um número entre 1 e 10.')
print('Será que você consegue adivinhar qual foi?')

gerador = randint(1,10)
acertou = False

while not acertou:
	n = int(input('\n\033[35mQual é seu palpite: \033[m'))

	if n == gerador:
		acertou = True

	else:	
		if n < gerador:
			print(f'Mais.. Tente outra vez.')
			tentativas += 1

		elif n > gerador:
			print(f'Menos.. Tente outra vez.')
			tentativas += 1

print('\033[1;35m---\033[m' * 11) #linha colorida(not important)
print(f'Acertou com {tentativas} tentativas.. \033[35m:)')

if tentativas <= 4:
	print('Muito Bom! Parabéns!\033[m')
else:
	print('Tente Novamente!\033[m')
print()

