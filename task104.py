#coding: utf-8
def leiaint(msg):
	ok = False
	while True:
		n = str(input(msg))
		if n.isnumeric():
			n = int(n)
			ok = True
		else:
			print('\033[31m> Erro! Digite um número inteiro válido <\033[m')
		if ok:
			break
	print('\033[31m---\033[m' *11)#linha decorativa colorida
	return n	
#programa principal 
n = leiaint('Digite um nº: ')
print(f'Você acabou de digitar o número {n}\n')