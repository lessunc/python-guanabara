#coding: utf-8
#------------------------------------------------------------------------------
#  Um programa que tem uma tupla preenchida com uma contagem por extenso de
#  zero à vinte. O programa recebe um número inteiro e retorna esse em extenso.
#------------------------------------------------------------------------------
#  Números por Extrenso (TUPLAS) - Exercício #072
#------------------------------------------------------------------------------
c = ('zero', 'um','dois', 'tres', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze',
'treze', 'quatorze', 'quinze', 'dezesseis', 
'dezesete', 'dezoito', 'dezenove', 'vinte')

print()
while True:
	n = int(input('Digite um número entre 0 e 20: '))
	if 0 <= n <= 20:
		break
	print('Tente Novamente. ',end='')

print('....' * 11) 
print(f'Voce digitou o número  {c[n]}') 
print('....' * 11) 
