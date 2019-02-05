#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que contém uma função chamada leiaint(), que funciona  
#  de forma semelhante à função input() do Python, porém fazendo a   
#  validação para aceitar somente um valor numérico inteiro.
#---------------------------------------------------------------------
#  Validando entrada de dados em Python - Exercício #104
#---------------------------------------------------------------------
def leiaint(msg):
	ok = False
	while True:
		n = str(input(msg))
		if n.isnumeric():
			n = int(n)
			ok = True
		else:
			print('\033[31m> Erro! Digite um número inteiro válido <\033[m')
		if ok:
			break
	print('\033[31m---\033[m' *11)#linha decorativa colorida
	return n	
#programa principal 
n = leiaint('Digite um nº: ')
print(f'Você acabou de digitar o número {n}\n')