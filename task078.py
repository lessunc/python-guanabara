#coding: utf-8
#-----------------------------------------------------------------------
#  Um programa que recebe cinco números guardando esses em uma lista, e 
#  retorna qual o maior e menor valor na lista e qual sua posição nessa.
#-----------------------------------------------------------------------
#  Maior e Menor valores na lista - Exercício #078
#-----------------------------------------------------------------------
valores = []
maior = menor = 0

for c in range(0, 5):
	valores.append(int(input(f'Digite um valor na posição {c+1}: ')))

	if c == 0:
		maior = menor = valores[0]
	else: 
		if valores[c] > maior:
			maior = valores[c]

		if valores[c] < menor:
			menor = valores[c]

print('\033[2;35m_._\033[m' *22)# linha colorida(not important)

print(f'Valores Digitados: {valores}')		
print(f'O Maior Valor Digitado Foi: {maior} Nas Posições: ',end=' ')

for e, v in enumerate(valores):
	if v == maior:
		print(f'{e +1}...',end='')

print()
print(f'O Menor Valor Digitado Foi: {menor} Nas Posições: ',end = '')

for e, v in enumerate(valores):
	if v == menor:
		print(f'{e +1}...',end=' ')

print()
print('\033[2;35m_._\033[m' *22)# linha colorida(not important)

