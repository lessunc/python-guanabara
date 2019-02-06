#coding: utf-8
#----------------------------------------------------------------------------------------
#  Um programa que contém uma função que recebe várias notas de alunos e retorna  
#  um dicionário contendo as informações :
#  • Quantidade notas |• Maior nota |• Menor nota |• Média geral |• Situação(opicional)  
#----------------------------------------------------------------------------------------
#  Ficha do Jogador - Exercício #105
#----------------------------------------------------------------------------------------
def notas(*num,sit=False):
	tot = 0
	dic = {}
	notas = num

	dic['total'] = len(notas)
	dic['maior'] = max(notas)
	dic['menor'] = min(notas)
	dic['media'] = int(sum(notas) / dic['total'])
	
	if sit:
		if dic['media'] >= 7:
			dic['Situação']= 'Boa'
		elif dic['media'] < 7 and dic['media'] > 5:
			dic['Situação']= 'Razoável'
		else:
			dic['Situação']= 'Ruim'
		print('----' *23)
	return dic

resp = notas(8.5, 10, 6.5, sit= True)
print(f'\033[35m{resp}\033[m')#colorido


