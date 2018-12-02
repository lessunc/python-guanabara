#coding: utf-8
#--------------------------------------------------------------
#  Um programa que recebe comprimento do cateto oposto e do 
#  cateto adjacente de um triângulo retângulo, calcula e 
#  retorna o comprimento da hipotenusa. 
#--------------------------------------------------------------
#  Catetos e Hipotenusa - Exercício #017
#--------------------------------------------------------------
import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(co,ca)

print('\033[2;36m')# código de cor

print(f'A hipotenusa vai medir {hipo:.2f}')
print('\033[m---' * 22)

