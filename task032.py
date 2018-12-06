#coding: utf-8
#-----------------------------------------------------------
#  Um programa que recebe um ano qualquer e retorna 
#  se ele é bissexto ou não.
#-----------------------------------------------------------
#  Ano Bissexto - Exercício #032
#-----------------------------------------------------------

ano = int(input('Qual ano vamos analizar? : '))
print('\033[35m---\033[m' * 22 ) #linha colorida(not important)

if ano % 4 == 0:
	print(f'O ano {ano} é BISSEXTO')
else:
	print(f'O ano {ano} não é BISSEXTO')

print('\033[35m---\033[m' * 22 ) #linha colorida(not important)

