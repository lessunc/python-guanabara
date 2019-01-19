#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que recebe nome e duas notas de vários alunos em uma 
#  lista composta, retornando um boletim com a média de cada aluno e
#  permitindo a visualização das notas de cada aluno individualmente.
#---------------------------------------------------------------------
#  Boletim com listas compostas - Exercício #089
#---------------------------------------------------------------------
dados = []

while True:
	cont = ' '
	nome = str(input('nome: '))
	nota1 = float(input('nota 1: '))
	nota2 = float(input('nota 2: '))
	media = (nota1 + nota2) / 2 

	dados.append([nome, [nota1, nota2], media])

	cont = str(input('\nQuer continuar? [s/n]: ')).strip()
	if cont == 'n':
		break

#(not important)
print('---' * 11)
print(f'{"Nº":<4} {"Nome":<10} {"Média":>8}')
print('---' * 11)

# nome e média geral
for e, d in enumerate(dados):
	print(f'{e:<4} {d[0]:<10} {d[2]:>8.1f}')

print('---' * 11)

#notas individuais
while True:
	opc = int(input('\nMostrar nota de qual aluno? (999 interrompe o programa) '))

	if opc <= len(dados)-1:
		print(f'Notas de {dados[opc][0]}: {dados[opc][1]}')
		print('---' * 11)

	if opc == 999:
		print('\n> Volte Sempre <')
		break

