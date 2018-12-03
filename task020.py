#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe o nome de 4 pessoas e retorna uma lista
#  com os 4 nomes em ordem sorteada.
#----------------------------------------------------------------
#  Sorteando uma ordem na lista - Exercício #020
#----------------------------------------------------------------
import random

n1 = str(input('Primeira Pessoa: '))
n2 = str(input('Segunda Pessoa : '))
n3 = str(input('Terceira Pessoa: '))
n4 = str(input('Quarta Pessoa: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(f'A nova ordem dos nomes será \033[2;35m{lista}\033[m:')
print('-----> END <-----')

