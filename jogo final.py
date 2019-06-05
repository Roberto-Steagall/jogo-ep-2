#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pygame Phisics Examples

Created on Wed May 29 13:28:27 2019

@author: victor
"""
import pygame
import math
import random

#Game Params
(width, height) = (1000,500)

screen = pygame.display.set_mode((width,height))
bgc = (255,255,255)
bg = pygame.image.load("imagem jogo final.png")

clock = pygame.time.Clock()

#Class Zone
class Particle(object):
	'''
	Classe da Partícula
	'''
	def __init__(self, x, y, size, speed=1, angle=0):
		self.x = x #posicao x
		self.y = y #posicao y
		self.size = size #tamanho
		self.color = (0,0,255) #cor
		self.thickness = 1 #espessura
		self.speed = speed #velocidade
		self.angle = angle #angulo de movimentação
		
	def display(self):
		'''
		Desenha o objeto na tela
		'''
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)
		
	def move(self):
		'''
		Movimenta o objeto
		'''
		self.x += round(math.sin(self.angle) * self.speed)
		self.y -= round(math.cos(self.angle) * self.speed)
		
	def bounce(self):
		'''
		Trata as colisões do objeto com as laterais da tela
		'''
		if self.x > width - self.size: #Direita
			return True
		elif self.x < self.size: #Esquerda
			return True
			
		if self.y > height - self.size: #Embaixo
			self.y = 2 * (height - self.size) - self.y
			self.angle = random.uniform(grau2rad(20), grau2rad(65))
			self.speed = -self.speed
			return False
		elif self.y < self.size: #Em cima
			self.y = 2 * self.size - self.y
			self.angle = random.uniform(grau2rad(20), grau2rad(65))
			self.speed = -self.speed
			return False

class Player(object):
	'''
	Classe de jogador
	'''
	def __init__(self, x, y, width, height, speed=1):
		self.x = x #posicao x
		self.y = y #posicao y
		self.width = width #comprimento
		self.height = height #altura
		self.color=(0,0,0) #cor
		self.speed = speed #velocidade
		
	def display(self):
		'''
		Desenha o objeto na tela
		'''
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
	
	def move(self, up):
		'''
		Movimenta o objeto
		'''
		if up:
			self.y -= self.speed
		else:
			self.y += self.speed
			
	def bounce(self):
		'''
		Trata as colisões do objeto com as laterais da tela
		'''
		if self.y > height: #Embaixo
			self.y = 0 - self.height
		if self.y < 0 - self.height:
			self.y = height #Em cima

#Function Zone			

def grau2rad(grau):
	'''
	Transformad de grau pra radiano
	'''
	return grau * math.pi / 180
	
def rad2grau(rad):
	'''
	Transforma de radiano pra grau
	'''
	return rad * 180 / math.pi
		
def collide_left(par,pla):
	'''
	Deprec
	Trata as colisões no lado esquerdo da tela
	'''
	dx = par.x -(pla.x + pla.width)
	dyt = par.y - pla.y
	dyb = par.y - (pla.y + pla.height)
	if dx <= 0:
		if dyt >= 0 or dyb >= 0:
			par.speed = -par.speed
			par.angle = random.uniform(math.pi/2, 3*math.pi/2)

def collide_right(par,pla):
	'''
	Deprec
	Trata as colisões no lado direito da tela
	'''
	dx = par.x - pla.x
	dyt = par.y - pla.y
	dyb = par.y - (pla.y - pla.height)
	#print("dx: %d\tdyt: %d\tdyb: %d" % (dx,dyt,dyb))
	if dx >= 0:
		if dyt >= 0 or dyb <= 0:
			par.speed = -par.speed
			par.angle = random.uniform(math.pi/2, 3*math.pi/2)

def collision(player, particle):
	'''
	Trata todas as colisões
	'''
	rtop = player.y
	rleft = player.x
	rright, rbottom = rleft + player.width/2, rtop + player.height/2
	cleft, ctop = particle.x - particle.size, particle.y - particle.size
	cright, cbottom = particle.x + particle.size, particle.y + particle.size
	
	if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
		return False
	
	for x in (rleft, rleft+player.width):
		for y in (rtop, rtop+player.height):
			if math.hypot(x-particle.x, y-particle.y) <= particle.size:
				return True
	
	if rleft <= particle.x <= rright and rtop <= particle.y <= rbottom:
		return True
		
	return False

#Creation Zone
par = Particle(500,250,15,angle=math.pi/4) #Cria a particula no centro da tela
player1 = Player(100,250-50,15,100) #Cria o jogador na esquerda, 2o parametro recebe o centro da tela menos metade do quarto
player2 = Player(900,250-50,15,100) #Cria o jogador da direita
run = True

#Main Loop
while run:
	for event in pygame.event.get(): #Event Catcher
		if event.type == pygame.QUIT:
			run = False
	pygame.display.set_caption('Tutorial 1') #Screen Title
	#screen.fill(bgc) #Background Fill
	screen.blit(bg,(0,0))
	pygame.display.update()
	
	pressed = pygame.key.get_pressed() #Key Getter
	if pressed[pygame.K_w]: player1.move(True)
	if pressed[pygame.K_s]: player1.move(False)
	if pressed[pygame.K_UP]: player2.move(True)
	if pressed[pygame.K_DOWN]: player2.move(False)
	par.move()
	
	player1.bounce()
	player2.bounce()
	
	result = par.bounce()

	#Win condition
	if result and par.x < 500:
		print('Player 2 ganhou!')
		run = False
	elif result and par.x > 500:
		print('Player 1 ganhou!')
		run = False

	#Display Zone
	player1.display()
	player2.display()
	par.display()
	
	#Collision Zone
	a = collision(player1, par)
	b = collision(player2, par)
	if a:
		print(a)
		par.x = player1.x + player1.width + 1
		par.speed = -par.speed
		par.angle = random.uniform(grau2rad(35), grau2rad(65))
	if b:
		print(b)
		par.x = player2.x - 1
		par.speed = -par.speed
		par.angle = random.uniform(grau2rad(35), grau2rad(65))
	
	pygame.display.flip() #Todas as atualizações de tela vem antes!
	clock.tick(250)
