#coding: utf-8
#----------------------------------------------------
#  Um programa que recebe o primeiro termo e a razão
#  de uma 'PA', retornando os 10 primeiros termos da
#  progressão usando a estrutura while.
#----------------------------------------------------
#  Progressão Aritmética v2.0 - Exercício #061
#----------------------------------------------------
print('\033[2;36m>> GERADOR DE P.A <<\033[m\n')

pt = int(input('Primeiro termo: '))
rz = int(input('P.A: '))
termo = pt
loop = 1

print('\033[2;36m><>\033[m' *22) #linha colorida(not important)

while loop <= 10:
	print(f'{termo} - ',end='')
	termo += rz
	loop += 1

print('FIM!') 	
print('\033[2;36m><>\033[m' *22) #linha colorida(not important)

