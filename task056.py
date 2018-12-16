#coding: utf-8
#----------------------------------------------------------------------
#  Um programa que recebe nome, idade, e sexo de 4 pessoas e retorna:
#  • A média de idade do grupo.
#  • O nome do homem mais velho do grupo.
#  • Quantidade de mulheres com menos de 20 anos.
#----------------------------------------------------------------------
#  Analizador Completo - Exercício #056
#----------------------------------------------------------------------
older = 0
oldername = ''
soma = 0
fem = 0

for c in range(1,5):
	
	print(f'\033[2;36m----- {c}º Pessoa -----\033[m')

	nome = str(input(f'Nome da {c}º pessoa:')).strip().title()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [Fem/Masc]:')).lower()
	soma += idade

	if c == 1 and sexo in 'masc':
		older = idade
		oldername = nome

	else:
		if idade > older:
			older = idade
			oldername = nome

		if sexo == 'fem':
			if idade <= 20:
				fem += 1

print(f'\033[2;36m---\033[m' *22) #linha colorida decorativa(not important)

print(f'A média de idade do grupo é de: {soma / 4}.')
print(f'O homem mais velho tem {older} anos e se chama {oldername}.')
print(f'Ao todo são {fem} mulheres com menos de 20 anos de idade.')

print(f'\033[2;36m---\033[m' *22) #linha colorida decorativa(not important)

