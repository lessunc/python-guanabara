#coding: utf-8
#-----------------------------------------------------------
#  Um algoritmo que recebe um valor de um produto e retorna 
#  seu novo valor com 5% de desconto 
#-----------------------------------------------------------
#  Calculando Descontos - Exercício #012
#-----------------------------------------------------------

preco = float(input('Digite um valor para ver seu desconto em 5% : '))
desconto = preco - ((preco*5) /100)

print(f'''Esse valor com 5% de desconto fica em: 
	\033[1;m{desconto} \033[m''')

