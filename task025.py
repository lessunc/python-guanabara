#coding: utf-8
#--------------------------------------------------------
#  Um programa que recebe um nome completo e  
#  confirma se existe ou não "Silva" no nome .	
#--------------------------------------------------------
#  Buscando uma string dentro da outra - Exercício #025
#--------------------------------------------------------

n = str(input('Nome Completo: ')).strip().lower()
s = 'silva' in n 

print(f'Sobre seu nome ter silva: {s}')

