#coding: utf-8
#--------------------------------------------------------------------------
#  Um programa que recebe 4 números em uma tupla e retorna: 
#  • Quantos números 9| • Posição do 1º número 3|• Quais os números pares|
#--------------------------------------------------------------------------
#  Maior e menor valores em Tupla - Exercício #075
#--------------------------------------------------------------------------
pares = 0
valor = (int(input('Digite um número: ')),
	int(input('Digite outro número: ')),
	int(input('Digite mais número: ')),
	int(input('Digite o último número: ')))
	
print('\033[2;35m====\033[m' *11) #linha colorida(not important)	
print(f'Você digitou os valores {valor}')
print(f'O valor 9 apareceu {valor.count(9)} vezes')

if 3 in valor:
	print(f'O valor 3 está na {valor.index(3)+1}ª posição')
else:
	print('O valor 3 não foi digitado em nenhuma posição!')
print('Os numeros pares digitados foram: ',end='')
for v in valor:
	if v % 2 == 0:
		print(f'{v}', end=' ')	
print()
print('\033[2;35m====\033[m' *11) #linha colorida(not important)

