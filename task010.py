#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe um valor em reais e calcula quantos
#  dólares é possível comprar com esse valor, considerando que
#  o dólar vale R$3,27.
#----------------------------------------------------------------
#  Conversor de Moedas - Exercício #010
#----------------------------------------------------------------

r = float(input('Quantos reais você quer converter para US$?  R$'))

print(f'Com R${r:.2f} você pode comprar US${r/3.27:.2f}')

