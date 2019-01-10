#coding: utf-8
#-----------------------------------------------------------------------------
#  Uma tupla com os 20 colocados da tabela de Campeonato Brasileiro de Futebol
#  na ordem da colocação cujo programa deve retornar:
#  • 5 primeiros colocados| • 4 últimos colocados| • Times em ordem alfabética| 
#  •Posição do time Chapecoense na Tabela.
#-----------------------------------------------------------------------------
#  Tuplas com time de Futebol - Exercício #073
#-----------------------------------------------------------------------------
from time import sleep

rk = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
'Flamengo', 'Vasco','Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 
'Bahía', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 
'Avaí', 'Ponte Preta', 'Atlético Goianiense')


print(f'\nRanking dos times de Futebol do Brasileirão:\033[2;35m \n{rk}')

sleep(2)
print(f'\n\033[mOs 5 primeiros são: \n\033[2;35m{rk[:5]}')
print()

sleep(2)
print(f'\033[mOs 4 últimos são: \n\033[2;35m{rk[-4:]}')
print()

sleep(2)
print(f'\033[mTimes em ordem alfabética: \n\033[2;35m{sorted(rk)}')
print()

sleep(2)
print(f'\033[2;35mO Chapecoense está na {rk.index("Chapecoense")+1}º posição')
print('>> fim do programa <<\033[m')

