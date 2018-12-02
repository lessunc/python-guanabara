#coding: utf-8
#-----------------------------------------------------------
#  Um programa que recebe 4 nomes e sorteia um deles. 
#-----------------------------------------------------------
#  Sorteando um item na lista - Exercício #019
#-----------------------------------------------------------
from random import choice

n1 = str(input('Primeira Pessoa: '))
n2 = str(input('Segunda Pessoa : '))
n3 = str(input('Terceira Pessoa: '))
n4 = str(input('Quarta Pessoa: '))

lista = [n1, n2, n3, n4]
pessoa = choice(lista)

print(f'O aluno escolhido foi: \033[2;35m{pessoa}\033[m:')
print('-----> END <-----')

