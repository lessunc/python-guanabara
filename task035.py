#coding: utf-8
#----------------------------------------------------------------------
#  Um programa que recebe o comprimento de 3 retas e retorna
#  se essas podem ou não formarem um triângulo.
#----------------------------------------------------------------------
#  Analizando um triângulo v1.0 - Exercício #035
#----------------------------------------------------------------------
l1 = float(input('Primeiro Seguimento: '))
l2 = float(input('Segundo Seguimento: '))
l3 = float(input('Terceiro Seguimento: '))

#linha formatada decorativa(not important)
print('\033[2;35m=-=\033[m' * 22)
print('Analizador De Triangulos')
print('\033[2;35m=-=\033[m' * 22)

#programa principal
if l1 <= l2 + l3 and l2 <= l1 + l3 and l3 <=l1 + l2:
	print('Os seguimentos acima podem formar triângulo!')
else: 
	print('Os seguimentos acima NÃO PODEM formar triângulo!')

print('\033[2;35m>>> END <<<\033[m') #linha colorida(not important)	

