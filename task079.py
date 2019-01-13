#coding : utf-8
#-----------------------------------------------------------------------
#  Um programa que recebe e cadastra vários valores em uma lista, não 
#  adicionando o mesmo valor mais de uma vez. O programa retorna todos
#  os valores únicos na lista em ordem crescente no final da execução.
#-----------------------------------------------------------------------
#  Valores únicos em uma Lista - Exercício #079
#-----------------------------------------------------------------------
numbers = []
while True:
	opc = ' '
	valor = (int(input('\nDigite um valor: ')))

	if valor not in numbers:
		numbers.append(valor)
		print('\033[36m> Valor adicionado com sucesso! <\033[m')
	else:
		print('\033[36mEsse valor já existe. Não será adicionado.\033[m :/')	

	while opc not in 'snSN':
		opc = str(input('Quer continuar? ')).strip()[0]	
	if opc in 'Nn':
		break

print('\033[36m---\033[m' *22)#linha decorativa(not important)
print(f'Voce digitou os valores {sorted(numbers)}\n')

