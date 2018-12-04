#coding: utf-8
#----------------------------------------------------
#  Um programa que recebe um número de 1 à 9999 e  
#  retorna cada um dos dígitos separadamente. Ex:
#----------------------------------------------------
#  n = 1324
#  unidade: 4, dezena: 2, centena: 3, milhar: 1
#----------------------------------------------------
#  Separando dígitos de um número - Exercício #023
#----------------------------------------------------

num = int(input('Informe um número de 0 à 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print(f'\nAnalisando o número {num}...')
print('\033[2;36m---\033[m' * 22)# linha decorativa(not important)

print(f'Unidade: {u} \nDezena: {d} ')
print(f'Centena: {c} \nMilhar: {m}')

print('\033[2;36m---\033[m' * 22)# linha decorativa(not important)

