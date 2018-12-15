#coding: utf-8
#---------------------------------------------------
#  Um programa que recebe uma frase e retorna se é 
#  um palíndromo ou não desconsiderando os espaços.
#---------------------------------------------------
#  Dectector de Palíndromo - Exercício #053
#---------------------------------------------------

frase = str(input('Digite uma frase ou palavra: ')).strip().upper()

cortado = frase.split()
unido = ''.join(cortado)
verso = ''

for c in range(len(unido)-1, -1, -1):
	verso += unido[c]

print('\033[2;35m---\033[m' *23) #linha colorida(not important)
print(f'{frase} Ao Contrário fica: {verso}')

if verso == unido:
	print('>> Temos um Palíndromo! <<')
else:
	print('>> Não é um Palíndromo! <<')

print('\033[2;35m---\033[m' *23)#linha colorida(not important)

