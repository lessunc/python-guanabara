#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe um número inteiro e mostra sua tabuada.
#----------------------------------------------------------------
#  Tabuada - Exercício #009
#----------------------------------------------------------------
n = int(input('Digite um número para ver sua tabuada: '))
print('=-'*13)

print(f'\033[35mA tabuada do número {n} é:\033[m')
print('=-'*13)

print(f'\033[35m{n} x 1 = {n*1}')
print(f'{n} x 2 = {n*2} \n{n} x 3 = {n*3}')
print(f'{n} x 4 = {n*4} \n{n} x 5 = {n*5}')
print(f'{n} x 6 = {n*6} \n{n} x 7 = {n*7}')
print(f'{n} x 8 = {n*8} \n{n} x 9 = {n*9}')
print(f'{n} x 10 = {n*10}\033[m\n ...end!')

print('=-'*13)

