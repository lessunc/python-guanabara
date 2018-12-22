#coding: utf-8
#------------------------------------------------------------
#  Um programa que recebe vários números inteiros e retorna
#  quantos números foram digitados e a soma entre eles.
#  O programa finaliza com o número 999 (condição de parada).
#------------------------------------------------------------
#  Tratando vários valores v1.0 - Exercício #064
#------------------------------------------------------------
soma = total = 0 
n = int(input('Digite Um Número \033[2;36m[999 para parar]:\033[m '))

while n != 999:
	total += 1
	soma += n
	n = int(input('Digite Um Número \033[2;36m[999 para parar]:\033[m '))

print(f'\nVocê Digitou {total} Números e a  Soma Entre Eles Foi: {soma} ')
print('\033[2;36m...\033[m' *22) #linha decorativa(not important)	

