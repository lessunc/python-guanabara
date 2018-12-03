#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe um nome completo e retorna:
#  • O nome em maiúsculo e minúsculo.
#  • Quantidade de letras ao todo sem contar os espaços.
#  • Quantidade de letras no primeiro nome.
#----------------------------------------------------------------
#  Analizador de Textos - Exercício #022
#----------------------------------------------------------------
from time import sleep

nome = str(input('Digite o nome completo: ')).strip()

print('\033[2;35m---\033[m' * 22)# linha colorida(not important)
print('Analizando seu nome...'.upper())
sleep(1)

print('\033[2;35m---\033[m' * 22)# linha colorida(not important)
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome em maiúscula é {nome.upper()}')

todo = len(nome) - nome.count(' ')
qto = nome.find(' ')
prim = nome.split()

print(f'Seu nome tem ao todo "{todo}" letras')
print(f'O primeiro nome tem "{qto}" letras')
print (f'O primeiro nome é {prim[0]}')
print('\033[2;35m---\033[m' * 22)# linha colorida(not important)

