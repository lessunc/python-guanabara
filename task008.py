#coding: utf-8
#--------------------------------------------
#  Um programa que recebe um valor em m² e 
#  exibe esse em centímetros e milímetros.
#--------------------------------------------
#  Medidas: km hm dam m dm cm mm 
#--------------------------------------------
#  Conversor de Medidas - Exercício 008
#--------------------------------------------

m = float(input('Uma distância em metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000

print('\033[35m---\033[m' * 22)#linha colorida(not important)

print(f'A medida de {m:.2f}m² corresponde a {cm}cm e {mm}mm')

print('\033[35m---\033[m' * 22)#linha colorida(not important)

