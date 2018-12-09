#coding: utf-8
#---------------------------------------------------------------------
#  Um programa que recebe o ano de nascimento de um jovem e informa
#  de acordo com a idade..
#  • Quanto tempo falta para esse se alistar ao serviço militar.
#  • Ou se é o ano de se alistar.
#  • E até mesmo se já passou do tempo do alistamento, e quanto tempo.
#---------------------------------------------------------------------
#  Alistamento Militar - Exercício #039
#---------------------------------------------------------------------
from datetime import date

nasc = int(input('Digite sua Data De Nascimento: '))
hoje = date.today().year
idade = hoje - nasc

print('\033[36m---\033[m' *22) #linha colorida(not important)
print(f'Quem nasceu em {nasc} tem {idade} anos em {hoje}.')

if idade == 18:
	print(f'>> Você tem que se alistar imediatamente! <<')

elif idade < 18:
	falta = 18 - idade
	print(f'>> Ainda Faltam {falta} anos para o alistamento! <<')
	print(f'... Seu alistamento será em {hoje + falta}')

elif idade > 18:
	foi = idade - 18
	print(f'>> Você já deveria ter se alistado à {foi} anos! <<')
	print(f'... Seu alistamento foi em {hoje - foi}')

print('\033[36m---\033[m' * 22) #linha colorida(not important)

