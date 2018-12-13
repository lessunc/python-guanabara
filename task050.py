#coding: utf-8
#---------------------------------------------------------------
#  Um programa que recebe 6 números inteiros e retorna a soma 
#  de todos os números pares desconsiderando os números ímpares.
#---------------------------------------------------------------
#  Soma dos pares - Exercício #050
#---------------------------------------------------------------
soma = 0
cont = 0

for n in range(1, 7):
	num = int(input(f'Digite o {n}º número: '))

	if num % 2 == 0:
		soma += num
		cont += 1

print('\033[36m---' * 22) #linha decorativa(not important)

if cont < 1:
	print(f'Nenhum número par foi digitado, não há soma, total: {soma}')

else:
	print(f'Foram digitados {cont} números pares, e a soma entre eles é: {soma}')
	
print('\033[36m---\033[m' * 22) #linha decorativa(not important)

