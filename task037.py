#coding: utf-8
#--------------------------------------------------
#  Um programa que recebe um número inteiro e uma 
#  de três opções relativas a base de conversão.
#  1- Binário|  2- Octal|  3- Exadecimal   
#--------------------------------------------------
#  Conversor de Bases Numéricas - Exercício #037
#--------------------------------------------------

n = int(input('Digite um valor qualquer inteiro: '))

print('''Escolha uma das bases para conversão\033[35m
	[1] Converter Para BINÁRIO
	[2] Converter Para OCTAL
	[3] Converter Para HEXADECIMAL\033[m''')

opcao = int(input('Sua opção: '))
print('\033[2;35m...\033[m' * 22 ) #linha colorida(not important)

if opcao == 1:
	print(f'"{n}"Convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
	print(f'"{n}"Convertido para OCTAL é igual a {oct(n)[2:]}')
elif opcao == 3:
	print(f'"{n}"Convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
	print('>> VALOR INVÁLIDO. Tente Novamente! <<')	

print('\033[2;35m...\033[m' * 22 ) #linha colorida(not important)

