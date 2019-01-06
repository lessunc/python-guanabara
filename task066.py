#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que recebe vários números inteiros, retornando quantos
#  números foram digitados e a soma entre eles desconsiderando o flag.
#  O programa deve finalizar com o número 999 (condição de parada).
#---------------------------------------------------------------------
#  Vários números com flag - Exercício #066
#---------------------------------------------------------------------	
print('\n\033[35m>>> Digite 999 Para Sair e Receber o Somatório <<<\033[m\n')

soma = total = 0
while True:
	n = int(input('Digite Um Número: '))
	if n == 999:
		break

	soma += n
	total += 1
print(f'\n\033[35mA Soma Dos {total} Valores Foi {soma}.\033[m')
print()	

