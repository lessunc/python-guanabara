#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que recebe nome e peso de várias pessoas em uma lista retornando:
#  • Quantas pessoas cadastradas| • Pessoas mais pesadas| • Pessoas mais leves
#---------------------------------------------------------------------------------
#  Lista composta e análize de dados - Exercício #084
#---------------------------------------------------------------------------------
dados = []
temp = []
maior = menor = 0

while True:
	opc = ' '
	temp.append(str(input('Nome: ')))
	temp.append(int(input('Peso: ')))

	if len(dados) == 0:
		maior = menor = temp[1]
	else: 
		if temp[1] > maior:
			maior = temp[1]
		if temp[1] < menor:
			menor = temp[1]

	dados.append(temp[:])
	temp.clear()
	while opc not in 'sn':
		opc = str(input('Quer Continuar? [s/n]: '))
	if opc == 'n':
		break

print('\033[35m===' *23)# linha decorativa(not important)
print(f'Dados: {dados}\033[m')

print(f'\nAo todo você cadastrou {len(dados)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de: ',end=' ')

for d in dados:
	if d[1] == maior:
		print(f'[{d[0]}]',end=' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de: ',end=' ')

for d in dados:
	if d[1] == menor:
		print(f'[{d[0]}]',end=' ')		
print()
print('\033[35m===\033[m' * 23)# linha decorativa(not important)

