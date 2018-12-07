#coding: utf-8
#--------------------------------------------------------------
#  Um programa que recebe 3 números e retorna o maior e menor. 
#--------------------------------------------------------------
#  Maior e menor valor - Exercício #033
#--------------------------------------------------------------

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#numero maior
maior = n1
if n2 > n1 and n2 > n3:
	maior = n2
if n3 > n1 and n3 > n2:
	maior = n3

print('==' *22)
print(f'O maior numero digitado foi: {maior}.')

#numero menor
menor = n1
if n2 < n1 and n2 < n3:	
	menor = n2
if n3 < n1 and n3 < n2:
	menor = n3	
print(f'E o menor número foi: {menor}.')

#linha formatada decorativa(not important)
print('==' *22)
print('{:^40} '.format('END'))
print('==' *22)

