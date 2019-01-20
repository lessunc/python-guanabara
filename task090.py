#coding: utf-8
#-----------------------------------------------------------
#  Um programa que recebe em um dicionário o nome, média e 
#  situação de um aluno retornando o conteúdo da estrutura.
#-----------------------------------------------------------
#  Dicionário em Python - Exercício #090
#-----------------------------------------------------------
dados = {}
dados['nome'] = str(input('Nome: ')).capitalize()
dados['media'] = float(input(f'Média de {dados["nome"]} '))

if dados['media'] <= 5:
	dados['situação'] = 'Reprovado'
elif dados['media'] <= 7:
	dados['situação'] = 'Recuperação'
else:
	dados['situação'] = 'Aprovado'

print('\033[1;35m=-=-\033[m' *11)# linha decorativa(not important)
for n, d in dados.items():
	print(f'  - {n} é igual a {d}')
print('\033[1;35m=-=-\033[m' *11)# linha decorativa(not important)

