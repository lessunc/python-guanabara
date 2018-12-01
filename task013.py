#coding: utf-8
#--------------------------------------------------------------
#  Um algoritmo que recebe o salário de um funcionário e mostra
#  seu novo salário com 15% de aumento. 
#--------------------------------------------------------------
#  Reajuste Salarial - Exercício #013
#-----------------------------------------------------------

atual = float(input('Qual o salário atual do funcionário? : R$'))
reajuste = atual * 15 /100

print(f'''Esse salário de {atual} foi atualizado devido ao aumento de 15% para :
	\033[1m"{atual + reajuste}" \033[m''')

