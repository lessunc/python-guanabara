#coding: utf-8
#------------------------------------------------------------
#  Um programa que recebe o primeiro termo e a razão de uma 
#  'PA', retornando os 10 primeiros termos da progressão.
#  O programa deve continuar recebendo os termos até que o
#  usuário escolha [0 termos] como opção para parar.
#------------------------------------------------------------
#  Super Progressão Aritmética v3.0 - Exercício #062
#------------------------------------------------------------
print('\033[2;36m>> GERADOR DE P.A <<\033[m\n')

pt = int(input('Primeiro termo: '))
rz = int(input('P.A: '))
termo = pt
loop = 1
total = 0
mais = 10

print('\033[2;36m><>\033[m' *22) #linha colorida(not important)
while mais != 0:
	total += mais

	while loop <= total:
		print(f'{termo}',end='')
	
		if loop < total:
			print(' - ',end='')
	
		else:
			print('  \033[2;36m <3\n',end ='')
		
		termo += rz
		loop += 1

	mais = int(input('\nQuantos termos você quer mostrar a mais: \033[m'))

print()	
print(f'>> Progressão Finalizada com {total} termos mostrados << ')
print('\033[2;36m><>\033[m' *22) #linha colorida(not important)


