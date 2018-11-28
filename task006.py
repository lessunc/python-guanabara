#coding: utf-8
#---------------------------------------------------------
#  Um algorítimo que recebe um número e retorna o dobro, 
#  o triplo e a raiz quadrada do seu valor.
#---------------------------------------------------------
#  Dobro, Triplo, Raiz Quadrada - Exercício #006
#---------------------------------------------------------

n = int(input('Digite um número qualquer: '))

dobro = n * 2  
triplo = n * 3 

print(f'O seu número foi: {n}\nO dobro do seu número é: {dobro},')
print(f'Sendo assim o triplo é: {triplo}\ne a raiz quadrada é: {pow(n, 1/2):.2f}')
print('>> FIM <<')

