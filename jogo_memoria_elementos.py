# -*- coding: utf-8 -*-



# Lembrete: Game Loop => Process Input -> Update Game -> Render

largura = 1000
altura = 600

branco = (255,255,255)
preto = (0,0,0)

import pygame
import random
import time

pygame.init()

#def tela_ganhou():
#	fonte = pygame.image.load("voce_ganhou.png").convert()
#	fonte.set_colorkey(fonte.get_at((0,0)))

def jogo():
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption("Jogo da Memória dos Elementos")
	ceu = pygame.transform.scale(pygame.image.load("ceu.jpeg").convert(), (largura, altura))

	clock = pygame.time.Clock()

	line = [21,221,421,621]
	lines = [40,210,380]
	a_squares = [False, False, False, False, False, False, False, False, False, False, False, False]
	counts = [0,4,8]
	clicked_images = []

	fogo = pygame.transform.scale(pygame.image.load("fogo.png").convert(), [160,160])
	terra = pygame.transform.scale(pygame.image.load("terra.png").convert(), [160,160])
	ar = pygame.transform.scale(pygame.image.load("ar.png").convert(), [160,160])
	agua = pygame.transform.scale(pygame.image.load("agua.png").convert(), [160,160])
	ying = pygame.transform.scale(pygame.image.load("ying.png").convert(), [160,160])
	yang = pygame.transform.scale(pygame.image.load("yang.png").convert(), [160,160])
	menu_sair1 = pygame.transform.scale(pygame.image.load("sair1.png").convert(), [250,200])
	menu_sair1.set_colorkey(menu_sair1.get_at((0,0)))
	menu_sair2 = pygame.transform.scale(pygame.image.load("sair2.png").convert(), [250,200])
	menu_sair2.set_colorkey(menu_sair2.get_at((0,0)))
	menu_novo_jogo1 = pygame.transform.scale(pygame.image.load("novo_jogo1.png").convert(), [250,200])
	menu_novo_jogo1.set_colorkey(menu_novo_jogo1.get_at((0,0)))
	menu_novo_jogo2 = pygame.transform.scale(pygame.image.load("novo_jogo2.png").convert(), [250,200])
	menu_novo_jogo2.set_colorkey(menu_novo_jogo2.get_at((0,0)))

	images = [fogo, fogo, terra, terra, ar, ar, agua, agua, ying, ying, yang, yang]
	random.shuffle(images) # Este comando "faz uma bagunça" na ordem dos elementos da lista images

	clicked_images = []

	count = 0
	p = []

	rodando = True




	while rodando:
		tela.fill(preto)
		tela.blit(ceu, [0,0])
		pygame.draw.rect(tela, (0,0,100), pygame.Rect(800,0,200,600))
		mousep = pygame.mouse.get_pos()
		clock.tick(30)
		count = 0
		if (mousep[0]>830) and (mousep[0]<980) and (mousep[1]>519) and (mousep[1]<575):
			tela.blit(menu_sair2,[780,450])

		else:
			tela.blit(menu_sair1,[780,450])

		if (mousep[0]>830) and (mousep[0]<980) and (mousep[1]>448) and (mousep[1]<505):
			tela.blit(menu_novo_jogo2,[780,380])

		else:
			tela.blit(menu_novo_jogo1,[780,380])

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rodando = False

			if event.type == pygame.MOUSEBUTTONUP:
				if (mousep[0]>830) and (mousep[0]<980) and (mousep[1]>519) and (mousep[1]<575):
					rodando = False

				elif (mousep[0]>830) and (mousep[0]<980) and (mousep[1]>448) and (mousep[1]<505):
					jogo()

				else:
					for o in lines:
						for i in line:
							if (mousep[0]>i) and (mousep[0]<i+160) and (mousep[1]>o) and (mousep[1]<o+160):
								if a_squares[count] != 'Fixed':	 # <- Sem essa condicional ocorre um bug muito esquisito. Ela faz com o que está 'fixed' permaneça 'fixed'				
									a_squares[count] = True

							count += 1		# A cada iteração do segundo loop for a variável count ganha +1 para que assim se possa fazer uma associação entre o conjunto de posições e um determinado número de índice de um elemento da lista de variáveis booleanas a_squares			
		count = 0

		for o in lines:
			for i in line:
				if (a_squares[count] == True) or (a_squares[count] == "Fixed"):
					tela.blit(images[count], [i,o])

				else:
					if (mousep[0]>i) and (mousep[0]<i+160) and (mousep[1]>o) and (mousep[1]<o+160):
						pygame.draw.rect(tela, (170,0,170), pygame.Rect(i,o,160,160))
				
					else:
						pygame.draw.rect(tela, (140,0,140), pygame.Rect(i,o,160,160))

				count += 1 

		if a_squares.count(True) == 2:
			for i in range(len(a_squares)):
				if a_squares[i] == True:
					clicked_images.append(images[i])
					p.append(i)

		if len(clicked_images) == 2:
			if clicked_images[0] != clicked_images[1]:
				pygame.display.update()	
				time.sleep(0.5)
				a_squares[p[0]] = a_squares[p[1]] = False
				p = []
				clicked_images = []

			else:
				a_squares[p[0]] = a_squares[p[1]] = "Fixed"
				p = []
				clicked_images = []
		
		
		print(mousep)
		if a_squares.count("Fixed")==len(a_squares):
			fonte = pygame.transform.scale(pygame.image.load("voce_ganhou.png").convert(), [300,250])
			fonte.set_colorkey(fonte.get_at((0,0)))
			tela.blit(fonte,[810,0])

		pygame.display.update()	
	
		
	pygame.quit()


jogo()
	
