#coding: utf-8
#------------------------------------------------------------------
#  Um programa que recebe idade e sexo de várias pessoas com opção 
#  de parar ou continuar os cadastros, retornando no final :
#------------------------------------------------------------------
#  • Quantas pessoas acima de 18 anos.
#  • Quantos homens cadastrados.
#  • Quantas mulheres com menos de 20 anos.
#------------------------------------------------------------------
#  Análise de dados do grupo - Exercício #069
#------------------------------------------------------------------
maior = wmenor = m = 0
while True:
	print('\033[35m>> Cadastre Uma Pessoa <<\033[m \n')

	idade = int(input('Idade: '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('Sexo: ')).strip().upper()[0]
		if sexo == 'M':
			m += 1
		if idade > 18:
			maior += 1
		if sexo == 'F' and idade < 20:
			wmenor += 1

	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer Continuar? [Sim/Não] : ')).strip().upper()[0]
	if resp == 'N':
		break

print('\033[35m==\033[m' *22) #linha decorativa(not important)
print(f'O total de pessoas com mais de 18 anos é {maior}.')
print(f'Ao todo temos {m} homens cadastrados.')
print(f'E temos {wmenor} mulheres menores de 20 anos')

print('\033[35m==\033[m' *22) #linha decorativa(not important)

