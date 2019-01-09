#coding: utf-8
#-----------------------------------------------------------------------------
#  Um programa que recebe o nome e preço de um produto, perguntando em 
#  seguida se deve continuar ou não os cadastros. No fim retorna:
#-----------------------------------------------------------------------------
#  • Total gasto| • Quantos produtos acima de R$1000.0| • Produto mais barato
#-----------------------------------------------------------------------------
#  Estatísticas em produtos - Exercício #070
#-----------------------------------------------------------------------------
total = mil = cont = menor = 0
cujo = ' '

while True:
	produto = str(input('Nome do Produto: ')).strip()
	preco = float(input('Preço: R$'))
	cont += 1
	total += preco

	if cont == 1 or preco < menor:
		menor = preco
		cujo = produto
	if preco >= 1000:
		mil += 1

	opc = ' '	
	while opc not in 'SN':
		opc = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
	if opc == 'N':
		break
		
print('{:-^56}'.format('\033[35m FIM DO PROGRAMA \033[m'))# linha decorativa(not important)
print()

print(f'total = R${total:.2f}')
print(f'temos {mil} valores custando mais de R$1000.00')
print(f'O produto mais barato é {cujo} que custa R${menor:.2f}')
print('----' *12)

