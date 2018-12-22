#coding: utf-8 
#----------------------------------------------------------------------
#  Um programa que recebe vários números e retorna a média entre eles,
#  e qual foi o menor e maior valor. O programa continua pedindo os
#  valores, ao menos que o usuário escolha parar o programa.
#----------------------------------------------------------------------
#  Maior e Menor valores - Exercício #065
#----------------------------------------------------------------------
cont = soma = 0
opc = 'S'
	
while opc == 'S':
	n = int(input('Digite um número: '))
	opc = str(input('\nQuer Continuar: [Sim/Não] ')).strip().upper()[0]
	cont += 1 
	soma += n
	media = soma / cont
	
	if cont == 1:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n

print('\033[2;35m===\033[m' *22) #linha colorida(not important)
print(f' Você digitou {cont} números, e a média foi {media:.2f}')
print(f' O maior valor foi {maior} e o menor foi {menor}')
print('\033[2;35m===\033[m' *22) #linha colorida(not important)

