#coding: utf-8
#-------------------------------------------------------------------------------------
#  Um programa que recebe em uma lista vários dicionários, contendo cadastrado o
#  nome, sexo, e idade de várias pessoas e retornando:
#  • Total de pessoas| • Média de idade| • Lista de mulheres| • Idades acima da média|
#-------------------------------------------------------------------------------------
#  Unindo dicionários e listas - Exercício #094
#-------------------------------------------------------------------------------------
from time import sleep
from operator import itemgetter

lista = []
lidade = []

while True:
	opc = ' '
	dic = {}
	dic['nome'] = str(input('Nome: ')).capitalize()

	while True:
		dic['sexo'] = str(input('Sexo [fem/masc]: ')).lower()[0]
		if dic['sexo'] in 'mf':
			break
		print('\033[31m>> Erro! Por Favor digite apenas (fem) ou (masc) <<\033[m')
	
	dic['idade'] = int(input('Idade: '))
	lidade.append(dic['idade'])
	lista.append(dic)

	while True:
		opc = str(input('\033[35mQuer continuar? [s/n]:\033[m')).lower()[0]
		print()

		if opc in 'sn':
			break
		print('\033[31m>> Erro! Por Favor digite apenas (s) ou (n) <<\033[m')

	if opc == 'n':
		break

media = sum(lidade)/len(lista)
print('\033[35m=-=-\033[m' *16)# linha decorativa(not important)

print(f'Ao todo {len(lista)} Pessoas Foram Cadastradas.')
print(f'A Média De Idade Do Grupo: {media:.0f}')

print(f'Mulheres Cadastradas: {", ".join(p["nome"] for p in lista if p["sexo"] == "f")}')
print('Pessoas que estão acima da média: ')

for p in lista:
	if p['idade'] >= media:
		print('   ')
		for k, v in p.items():
			print(f'{k} = {v},', end= ' ')
		print()	

print('\033[35m=-=-\033[m' *16)# linha decorativa(not important)
print(f'> FINALIZADO.')

