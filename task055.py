#coding: utf-8
#----------------------------------------------
#  Um programa que recebe o peso de cinco 
#  pessoas e retorna o maior e menor peso.
#----------------------------------------------
#  Maior e menor da sequência - Exercício #055
#----------------------------------------------
maior = 0
menor = 0

for c in range(1, 6):
	peso = float(input(f'Peso da {c}º Pessoa: '))

	if c == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso

print('\033[35m...\033[m' * 22)#linha colorida(not important)

print(f'O maior peso foi de: {maior} Kg')
print(f'O menor peso foi de: {menor} Kg')

print('\033[35m...\033[m' * 22) #linha colorida(not important)

