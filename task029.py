#coding: utf-8
#----------------------------------------------------------------------
#  Um programa que recebe a velocidade de um carro. Se essa ultrapassar
#  80Km/h, uma mensagem deverá ser retornada avisando que o carro foi
#  multado. A multa deverá custar R$7,00 por cada Km/h acima do limite.
#----------------------------------------------------------------------
#  Radar eletrônico - Exercício #029
#----------------------------------------------------------------------
from time import sleep

vel = int(input('Qual a velocidade atual do carro? '))
print('\033[1;31m===\033[m' *22) #linha decorativa(not important)

if vel >= 81:
	
	print('MULTADO! Você excedeu o limite de 80 Km/h\n')

	print('CALCULANDO VALOR DA MULTA...')
	sleep(2)
	print(f'Você deve pagar uma multa de R$ {(vel - 80) *7},00')

else: 
	print('Velocidade Permitida...')

print('Tenha um bom dia! Dirija com segurança!  <3\n')
print('\033[1;31m===\033[m' *22) #linha decorativa(not important)

