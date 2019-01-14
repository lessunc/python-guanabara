#coding: utf-8
#---------------------------------------------------------------------------------
#  Um programa que recebe e cadastra cinco valores em uma lista, armazenando os
#  valores em ordem crescente já na posição correta de inserção, sem usar sort()
#  ou qualquer outra função para tal. No fim da execução retorna a lista ordenada. 
#---------------------------------------------------------------------------------
#  Lista ordenada sem repetições - Exercício #080
#---------------------------------------------------------------------------------
valores = []
for c in range(0,5):
	num = int(input('Digite um valor: '))

	if c == 0 or num > valores[-1]:
		valores.append(num)
		print('adicionado ao final da lista!\n')
	else:
		cont = 0
		while cont < len(valores):
			if num <= valores[cont]:
				valores.insert(cont, num)
				print(f'adicionado na posição {cont} da lista')
				break
			cont += 1

print(f'\nOs valores digitados em ordem ficam.. \033[35m{valores} .')
print('\033[35m~~~\033[m' * 22)# linha decorativa(not important)	
print()

