#coding: utf-8
#-----------------------------------------------------------
#  Um programa que recebe a distância de uma viagem em km, 
#  e calcula o preço da viagem cobrando R$0.50 por Km para
#  viagens de até 200 Km e R$0.45 para viagens mais longas.
#-----------------------------------------------------------
#  Custo da viagem - Exercício #031
#-----------------------------------------------------------

n = float(input('Qual a distância da viagem? '))
print('\033[1;36m---\033[m' * 22 ) #linha colorida(not important)

print(f'Voce está prestes a começar uma viagem de {n:.2f} Km\033[m')

if n <= 200:
	preco = n * 0.50
else:
	preco = n * 0.45

print(f'E o preço da sua passagem será de {preco:.2f}')
print('\033[1;36m---\033[m' * 22 ) #linha colorida(not important)

