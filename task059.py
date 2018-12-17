#coding: utf-8
#------------------------------------------------------------------
#  Um programa que recebe dois valores e retorna 
#  um menu enumerado, e com as seguintes opções: 
#------------------------------------------------------------------
#  1- Somar| 2- Multiplicar|3- Maior| 4- Novos Números|5- Sair
#------------------------------------------------------------------
#  Criando um Menu de Opções - Exercício #059
#------------------------------------------------------------------
from time import sleep

pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
opc = 0

while opc != 5:
#print do menu para escolher a opção
	print('Opções: \033[35m')
	sleep(1)
	print('''
[1]  Somar 
[2]  Multiplicar 
[3]  Maior Número 
[4]  Novos Números 
[5]  Nenhuma Opção (sair)\033[m''')

	opc = int(input('Escolha uma opção: '))	
	print('\033[1;35m...\033[m' *14) #linha colorida(not important)
	sleep(0.5)
	
	if opc == 1:
		print(f'{pv} mais {sv} é igual a {pv + sv}.')

	elif opc == 2:
		print(f'{pv} multiplicado por {sv} é igual a {pv * sv}.')

	elif opc == 3:
		if pv > sv:
			print(f'-- {pv} é maior que {sv} --')

		if pv < sv:
			print(f'-- {sv} é maior que {pv} --')

		if pv == sv:
			print(' Nenhum Maior.. Os dois números são Iguais.')

	elif opc == 4:
		print('\033[35m >>> Informe os números novamente <<<\033[m')

		pv = int(input('Primeiro valor: '))
		sv = int(input('Segundo valor: '))

	elif opc == 5:
		print('\033[35mOpção 5 ...Fechando \033[m ')
		break
	
	else:
		print('Opção Inválida. Por favor escolha uma opção abaixo:')
	print('\033[1;35m...\033[m' *14) #linha colorida(not important)

sleep(1)
print('>>> PROGRAMA FINALIZADO \033[1;35m =)\033[m\n')

