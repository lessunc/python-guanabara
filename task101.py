#coding: utf-8

def voto(ano):
	from datetime import date
	n = date.today().year - ano
	print(f'Com {n} anos:', end=' ')

	if n < 18:
		print('NÃO VOTA!')
	if n >= 18 and n < 65 :
		print('VOTO OBRIGATÓRIO!')
	if n > 70:
		print('VOTO OPCIONAL!')
	print()
	
print('---' *11)
voto(int(input('Ano de Nascimento: ')))

