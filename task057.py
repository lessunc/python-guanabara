# coding: utf-8
#-----------------------------------------------------------------
#  Um programa que recebe o sexo de uma pessoa mas só
#  aceite os valores 'M' 'F'. Caso esteja errado o programa
#  deverá pedir a digitação até receber um valor correto.
#------------------------------------------------------------------
#  Validação de Dados - Exercício #057
#------------------------------------------------------------------

sexo = str(input('Por favor informe seu sexo [F/M]: ')).strip().upper()[0]

while sexo not in 'FM':
	sexo = str(input('Opção Inválida! Por favor informe seu sexo: [F/M]')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
 
 