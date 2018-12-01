#coding: utf-8
#------------------------------------------------------------------------
#  Um programa que recebe a distância em Km percorridos por um carro e a 
#  quantidade de dias pelos quais o carro foi alugado, e calcula o preço
#  final sabendo que o carro custa R$60 por dia, e R$0.15 por km rodados.
#------------------------------------------------------------------------
#  Aluguel de Carros - Exercício #015
#------------------------------------------------------------------------

dias = int(input('Quantos dias alugado? ')) 
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
 
print(f'\033[34mO total a pagar é de: R${pago:.2f}\033[m')
print('=-' * 16)

