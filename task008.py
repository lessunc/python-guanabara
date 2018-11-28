#coding: utf-8
#------------------------------------------
#  Um programa que recebe um valor em m² e o
#  exibe em centímetros e milímetros
#------------------------------------------
#  Conversor de Medidas - Exercício 008
#------------------------------------------
#  >> escala de medidas para auxilio <<
#  >> km hm dam m dm cm mm <<
#------------------------------------------

m = float(input('Uma distância em metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000

print('\033[35m---\033[m' * 22)
print(f'A medida de {m:.2f}m² corresponde a {cm}cm {mm}mm')
print('\033[35m---\033[m' * 22)

