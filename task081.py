#coding: utf-8
#--------------------------------------------------------------------------------
#  Um programa que recebe e cadastra vários números em uma lista, retornando:
#  • Total de valores | • Lista em ordem decrescente| • Se tem 5 na lista 
#--------------------------------------------------------------------------------
#  Extraindo dados de uma Lista - Exercício #081
#--------------------------------------------------------------------------------
num = []
while True:
	opc = ' '
	n_opc = ' '

	while not n_opc.isdigit():
		n_opc = input('Digite um valor: ')
	num.append(int(n_opc))

	while opc not in 'SN':
		opc = str(input('\nQuer Continuar? [S/N]: ')).strip().upper()[0]
	if opc == 'N':
		break

print('\033[35m~~~\033[m' * 22)# linha decorativa(not important)	
print(f'Você digitou {len(num)} valores.')
print(f'Os valores em ordem decrescente são {sorted(num, reverse = True)} ')

if num.count(5) >= 1:
	print('O número 5 faz parte da lista.')
else:
	print('O número 5 não foi encontrado na lista.\n')

