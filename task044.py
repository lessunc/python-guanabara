#coding: utf-8
#------------------------------------------------------------
#  Um programa que calcula o valor a ser pago por um produto 
#  considerando o seu preço normal e condição de pagamento:
#------------------------------------------------------------
#  • à vista dinheiro/cheque: 10% desconto
#  • à vista no cartão: 5% de desconto
#  • em até 2 vezes no cartão: preço normal
#  • 3 vezes ou mais no cartão: 20% juros
#------------------------------------------------------------
#  Gerador de Pagamentos - Exercício #044
#------------------------------------------------------------

valor = int(input('Valor das compras: '))

print('\033[31m_._.\033[m' *22)# linha decorativa(not important)

print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')

print('\033[31m_._.' *22)# linha decorativa(not important)

opcao = int(input('Qual a opção? :\033[m ')) 

if opcao == 1:
	prc = valor * 10 / 100 
	print(f'\nVoce recebeu um desconto de 10% O valor agora é de R${valor - prc:.2f}.')

elif opcao == 2:
	prc = valor * 5 / 100
	print(f'\nVoce recebeu um desconto de 5% O valor agora é de R${valor - prc:.2f}.')

elif opcao == 3:
	prc = valor / 2
	print(f'\nSua compra será parcelada em 2x de R${prc:.2f} sem juros.')

elif opcao == 4:
	prc = valor + (valor * 20 / 100)

	vezes = int(input('\033[31mQuantas Parcelas? :\033[m '))
	parcela = prc / vezes

	print(f'\nSua compra será parcelada em {vezes}x de R${parcela:.2f}')
	print(f'Com essa opção você tem 20 % de juros.. o valor final será: R${prc:.2f}')

else:
	print('>>> Opção Inválida <<<')

print('\033[31m_._.\033[m' *22)# linha decorativa(not important)

