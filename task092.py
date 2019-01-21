#coding: utf-8
#-------------------------------------------------------------------------------------
#  Um programa que recebe nome, ano de nascimento, e carteira de trabalho em um 
#  dicionário, cadastrando também o ano de contratação e o salário no caso da CTPS
#  ser maior que 0. Calculando e acresentando a idade atual e idade na aposentadoria.
#-------------------------------------------------------------------------------------
#  Cadastro de Trabalhador em Python - Exercício #092
#-------------------------------------------------------------------------------------
from datetime import date
dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc 
dados['ctps'] = int(input('Nº Carteira de Trabalho (0 não tem): '))


if dados['ctps'] != 0:
	dados['contrato'] = int(input('Ano de Contratação: '))
	dados['salário'] = float(input('Salário: R$' ))
	apos = dados['contrato'] + 35
	dados['aposentadoria'] = apos - date.today().year + dados['idade']

print('\033[2;36m===\033[m' *22)#linha decorativa(not important)

for k, v in dados.items():
	print(f'{k} ------- {v}')

print('\033[2;36m===\033[m' *22)#linha decorativa(not important)

