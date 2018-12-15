#coding: utf-8
#----------------------------------------------------
#  Um programa que recebe o ano de nascimento de  
#  sete pessoas retornando quantas pessoas ainda não 
#  atingiram a maioridade, e quantas já são maiores.
#----------------------------------------------------
#  Grupo da Maioridade - Exercício #054
#----------------------------------------------------
from datetime import date

maiores = 0
menores = 0

for c in range(1, 8):
	nasc = int(input(f'Data De Nascimento Da {c}º Pessoa: '))
	hoje = date.today().year
	idade = hoje - nasc

	if idade >= 18:
		maiores += 1
	else:
		menores += 1

print(f'Menores de idade: {menores}')
print(f'Maiores de idade: {maiores}')

