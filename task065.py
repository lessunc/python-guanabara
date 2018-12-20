#coding: utf-8 
#---------------------------------------------------------------------
#  Um programa que recebe vários números e retorna a média entre eles,
#  e qual foi o menor e maior valor. O programa pede os valores no fim
#  de cada execução, ao menos que o usuário escolha parar o programa.
#---------------------------------------------------------------------
#  Maior e Menor valores - Exercício #065
#---------------------------------------------------------------------
cont = soma = 0
opc = 'S'
	
while opc == 'S':
	n = int(input('Digite um número: '))
	opc = str(input('Quer Continuar: [Sim/Não] ')).strip().upper()[0]
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

print()
print('\033[2;35m===\033[m' *22) #linha colorida(not important)
print(f' Você digitou {cont} números, e a média foi {media}')
print(f' O maior valor foi {maior} e o menor foi {menor}')
print('\033[2;35m===\033[m' *22) #linha colorida(not important)
