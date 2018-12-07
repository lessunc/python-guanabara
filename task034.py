#coding: utf-8
#----------------------------------------------------------------------
#  Um algoritmo que recebe o salário de um funcionário e calcula o
#  valor do aumento. Sendo um aumento de 10% para salários superiores
#  à R$1.250,00 e 15% para salários inferiores e iguais a esse.
#----------------------------------------------------------------------
#  Aumento multiplos - Exercício #034
#----------------------------------------------------------------------
from time import sleep

salario = float(input('Qual o salário a ser ajustado?  R$ '))

if salario > 1250:
	desconto = (salario * 10)/100
elif salario <= 1250:
	desconto = (salario * 15)/100

print('\033[1;35mAjustando Salário...\033[m')
sleep(1)

print('\033[35m...\033[m' *22)# linha colorida(not important)
print(f'Quem ganhava "R${salario:.2f}" passará a ganhar "R${salario + desconto:.2f}"')
print('\033[35m...\033[m' *22)# linha colorida(not important)

