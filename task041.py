#coding: utf-8
#-----------------------------------------------------------------------
#  Um programa que recebe uma data de nascimento e retorna sua categoria
#  de acordo com a idade calculada apartir da dessa data.
#-----------------------------------------------------------------------
#  Até 9 anos: Mirim | Até 14 anos:Infantil | Até 19 anos: Júnior
#  Até 25 anos: Sênior | Acima: Master
#-----------------------------------------------------------------------
#  Classificando Atletas - Exercício #041
#-----------------------------------------------------------------------
from datetime import date

hoje = date.today().year
nasc = int(input('Data De Nascimento: '))
idade = hoje - nasc

print('\033[2;35m---\033[m'* 22)# linha colorida(not important)
print(f'O atleta tem \033[2;35m"{idade}"anos\033[m')# \033m - código de cor

if idade <= 9:
	print('Classificação: MIRIM')
elif 9 < idade <= 14:
	print('Classificação: INFANTIL')
elif 14 < idade <= 19:
	print('Classificação: JUNIOR')
elif 19 < idade <= 25:
	print('Classificação: SÊNIOR')
else:
	print('Classificação: MASTER')	

print('\033[2;35m---\033[m' *22)# linha colorida(not important)

