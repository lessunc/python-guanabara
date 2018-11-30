#coding: utf-8
#----------------------------------------------------------------
#  Um programa que recebe altura e largura em m² e calcula a área
#  e a quantidade de tinta necessária para pintá-la, considerando 
#  que cada litro de tinta pinta uma área de 2m².
#----------------------------------------------------------------
#  Pintando Parede - Exercício #011
#----------------------------------------------------------------

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt

print(f'\nA área da sua parede é {area:.2f}m²')
print(f'É necessário {area/2:.1f}l de tinta para pintar essa parede.')

