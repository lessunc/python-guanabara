#coding: utf-8 
#----------------------------------------------------------------
#  Um programa que recebe uma frase e retorna:
#  • Quantidade de letras 'A' na frase
#  • Posição em que a letra 'a' aparece na primeira e última vez
#----------------------------------------------------------------
#  Primeira e última ocorrência em uma string - Exercício #026
#----------------------------------------------------------------

frase = str(input('Digite uma frase qualquer: ')).strip().lower()

print('\033[2;36m=-=-\033[m' *14) #linha colorida(not important)

print(f'A letra "A" aparece {frase.count("a")} vezes na frase digitada')
print(f'A primeira letra "A" aparece na posição: {frase.find("a")+1}')
print(f'A ultima letra "A" aparece na posição: {frase.rfind("a")+1}')

print('\033[2;36m=-=-\033[m' *14) #linha colorida(not important)

