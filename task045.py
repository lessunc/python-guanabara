#coding: utf-8
#---------------------------------------------------------------------------
#  Um programa que joga "JOKENPO" importando o randint da biblioteca random. 
#---------------------------------------------------------------------------
#  GAME >> pedra| papel| tesoura - Exercício #045
#---------------------------------------------------------------------------
from time import sleep
from random import randint

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''\033[1;35mSuas Opções:

\033[1;35m[ 0 ] \033[36mPEDRA
\033[1;35m[ 1 ] \033[36mPAPEL
\033[1;35m[ 2 ] \033[36mTESOURA\033[1;35m
''')

jogador = int(input('Qual é a sua jogada? '))

# print decorativo(not important)
print('\033[1;36mJO\033[m')
sleep(0.5)
print('\033[1;35mKEN\033[m')
sleep(0.5)
print('\033[1;36mPO\033[m')
sleep(0.5)
print('\033[36m=-=-\033[m' * 11)

print(f'''\033[35mVOCÊ JOGOU >>>>>\033[m {lista[jogador]}
\033[35mO COMPUTADOR JOGOU  >>>>>\033[m {lista[computador]}''')

print('\033[36m=-=-\033[m' * 11)# linha colorida(not important)

if computador == 0: #COMPUTADOR JOGA PEDRA <<<<<<<<<
	if jogador== 0:
		print('\033[35mNinguem Ganhou.. EMPATE!\033[m')
	elif jogador == 1:
		print('\033[35mVOCÊ GANHOU!\033[m')
	elif jogador == 2:
		print('\033[35mVOCÊ PERDEU!\033[m')

elif computador == 1: #COMPUTADOR JOGA PAPEL <<<<<<<<<
	if jogador == 0:
		print('\033[35mVOCÊ PERDEU!\033[m')
	elif jogador == 1:
		print('\033[35mNinguem Ganhou.. EMPATE!\033[m')
	elif jogador == 2:
		print('\033[35mVOCÊ GANHOU!\033[m')

elif computador == 2: #COMPUTADOR JOGA TESOURA <<<<<<<<
	if jogador == 0:
		print('\033[35mVOCÊ GANHOU!\033[m')
	elif jogador == 1:
		print('\033[35mVOCÊ PERDEU!\033[m')
	elif jogador == 2:
		print('\033[35mNinguem Ganhou.. EMPATE!\033[m')

print('\033[36m=-=-\033[m' * 11)# linha colorida(not important)

