#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe um valor em reais e calcula quantos
#  dólares é possível comprar com esse valor, considerando que
#  o dólar vale R$3,27.
#----------------------------------------------------------------
#  Conversor de Moedas - Exercício #010
#----------------------------------------------------------------

r = float(input('Quanto você quer converter para US$? R$'))

print('\033[2;36m><\033[m' * 22)
print(f'Com R${r:.2f} você pode comprar {r/3.20:.2f} US$')
print('\033[2;36m><\033[m' * 22)

