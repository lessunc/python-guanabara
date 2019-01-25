#coding: utf-8
#---------------------------------------------------------------------------
#  Um programa com uma função que recebe 3 parâmetros: início, fim, e passo
#  e realiza a contagem. São 3 contagens através da função, sendo elas:
#  • De 1 à 10 com 1 passo | • De 10 à 0 com 2 passos | • Personalizada 
#---------------------------------------------------------------------------
#  Função de Contador - Exercício #098
#---------------------------------------------------------------------------
from time import sleep

def linha():
	print('\033[35m-=-=\033[m' * 11)

def contador(i, f, p):
	linha()
	print(f'CONTAGEM DE {i} ATÉ {f} DE {p} EM {p}')

	if p < 0:
		p *= -1
	if p == 0:
		p = 1
	if i < f:
		c = i
		while c <= f:
			print(c, end=' ', flush=True)
			sleep(0.2)
			c += p
		print('FIM')
	if i > f:
		c = i
		while c >= f:
			print(c, end=' ', flush=True)
			sleep(0.2)
			c -= p
		print('FIM')
		
contador(1, 10, 1)
contador(10, 0, 2)

linha()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
linha()

