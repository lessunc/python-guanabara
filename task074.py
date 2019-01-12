#coding: utf-8
#-----------------------------------------------------------------------------
#  Um programa que gera 5 números aleatórios em uma tupla retornando a 
#  listagem desses números e indicando o menor e maior valor gerado.
#-----------------------------------------------------------------------------
#  Maior e menor valores em Tupla - Exercício #074
#-----------------------------------------------------------------------------
from random import randint
print('\033[2;36m===\033[m' * 11)#linha decorativa(not important)

n = (randint(1,10), randint(1,10),randint(1,10),
randint(1,10), randint(1,10))

print(f'Valores gerados: \n{n}')
print(f'\nO maior valor do random foi {max(n)}.')
print(f'E o menor valor foi {min(n)}.')

print('\033[2;36m===\033[m' * 11)#linha decorativa(not important)

