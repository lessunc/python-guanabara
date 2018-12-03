#coding: utf-8
#----------------------------------------------------------------
#  Um programa que abre e reproduz o áudio de um arquivo MP3.
#----------------------------------------------------------------
#  Tocando um MP3 - Exercício #021
#----------------------------------------------------------------
import pygame, mutagen.mp3

opc = str(input('\n\033[35mDigite bora, para curtir um GreenDayzinho <3: \033[m')).lower()[0]

if opc == 'b':

	#linha colorida	com frase centralizada(not important)
	print('\033[2;35;45m>>>{:^60}<<<\033[m'.format('BOM SOM'))

	#instrução para parar com código de cor(opcional)
	print('\033[35m>> Qualquer botão para parar <<\033[m\n')
	
	mp3file = 'task021guns.mp3'
	pygame.mixer.init(frequency=mutagen.mp3.MP3(mp3file).info.sample_rate)
	pygame.mixer.music.load(mp3file)
	pygame.mixer.music.play()
	pygame.init()
	pygame.event.wait()

print('Thanks for listening.')	

