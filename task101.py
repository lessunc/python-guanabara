#coding: utf-8

def voto(ano):
	from datetime import date
	n = date.today().year - ano

	if n < 16:
		print(f'Com {n} anos: NÃO VOTA!\n')
	elif 16 <= n < 18 or n > 65:
		print(f'Com {n} anos: VOTO OPCIONAL!\n')
	else:
		print(f'Com {n} anos: VOTO OBRIGATÓRIO!\n')

print('---' *11)
voto(int(input('Ano de Nascimento: ')))

