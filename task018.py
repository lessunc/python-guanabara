#coding: utf-8
#--------------------------------------------------------------
#  Um programa que recebe o valor de um ângulo e retorna o valor
#  do seno, cosseno e tangente desse ângulo. 
#--------------------------------------------------------------
#  Seno, Cosseno e Tangente - Exercício #018
#--------------------------------------------------------------
from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
print('\033[36m....\033[m' * 16)# linha colorida(not important)

seno = sin(radians(angulo))
print(f'O seno de {angulo} é {seno:.2f}')

cos = cos(radians(angulo))
print(f'O cosseno de {angulo} é {cos:.2f}')

tan = tan(radians(angulo))
print(f'O tangente de {angulo} é {tan:.2f}')

print('\033[36m....\033[m' * 16)# linha colorida(not important)

