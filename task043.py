#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe peso e altura de uma pessoa calculando 
#  o IMC e retornando seu status de acordo com a tabela de IMC.
#----------------------------------------------------------------
#  Índice de Massa Corporal - Exercício #043
#----------------------------------------------------------------
peso = float(input('Qual o seu peso? (kg): '))
alt = float(input('Qual sua altura? (cm): '))
imc = peso / (alt * alt)

print('\033[1m---\033[m' *22) #linha colorida(not important)
print(f'Seu Índice De Massa Corporal (IMC) é de "{imc:.1f}"')

if imc < 18.5:
	print('Abaixo Do Peso!')

elif 18.5 <= imc < 25.0:
	print('Peso Ideal!')

elif 25.0 <= imc < 30.0:
	print('Sobrepeso!')

elif 30.0 <= imc < 40.0:
	print('Obesidade!')

else:
	print('Obesidade Mórbida!')

print('\033[1m---\033[m' *22) #linha colorida(not important)

