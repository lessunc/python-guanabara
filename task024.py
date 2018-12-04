#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe o nome de uma cidade e confirma se essa
#  começa ou não com o nome "Santo".
#----------------------------------------------------------------
#  Verificando as primeiras letras de um texto - Exercício #024
#----------------------------------------------------------------

c = str(input('Onde você vive?')).strip().lower()
print(c[:5] == 'santo')
print() 

