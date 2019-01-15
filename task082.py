#coding: utf-8
#------------------------------------------------------------------
#  Um programa que recebe e cadastra vários números em uma lista
#  separando os valores pares e ímpares em listas diferentes .
#------------------------------------------------------------------
#  Dividindo valores em listas - Exercício #082
#------------------------------------------------------------------
l1 = []
l2 = []
l3 = []
while True:
	opc = ' '
	l1.append(int(input('Digite um número: ')))

	while opc not in 'sn':
		opc = str(input('Quer continuar? [s/n]: '))
		print('{:^26}'.format('\033[34m≈≈≈\033[m'))# decorativo(not important)
	if opc == 'n':
		break
for c in l1:
	if c % 2 == 0:
		l2.append(c)
	else:
		l3.append(c)

print(f'\nA lista completa é {l1}')
print(f'A lista de pares é {l2}')
print(f'A lista de ímpares é {l3}\n')
print('\033[1;34m~~\033[m' *22)# decorativo(not important)

