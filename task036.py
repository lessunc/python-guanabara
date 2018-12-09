#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que recebe o valor da casa, salário do comprador, e 
#  em quantos anos o comprador deseja pagar pela casa. O programa  
#  deve aprovar o empréstimo. Caso a prestação exceder 30% do salário 
#  o empréstimo deverá ser negado.
#---------------------------------------------------------------------
#  Aprovando Empréstimo - Exercício #036
#---------------------------------------------------------------------
from time import sleep

nome = str(input('Qual o seu primeiro nome? '))	
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja parcelar? '))

parcela = casa / (anos * 12)
minimo = salario * 30 / 100

print('\033[36mAGUARDE... CALCULANDO...\033[m')
sleep(1)

print('\033[36m...\033[m' *22)

# verificando se aprovado ou recusado apartir dos 30% do salário.
if parcela <= minimo:
	print(f'A parcela é de: "{parcela:.2f}" não excede os 30% do seu salario!')
	print('\033[36m--- Parabéns! seu empréstimo foi aprovado ---\033[m')

else:
	print(f'A parcela de {parcela:.2f} excede 30% do seu salario!')
	print(f'\033[36mDesculpe. Seu Empréstimo foi recusado.\033[m')

print('\033[36m...\033[m' *22)

