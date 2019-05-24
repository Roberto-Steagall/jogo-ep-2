# -*- coding: utf-8 -*-
"""
Created on Thu May 23 18:37:19 2019

@author: breno
"""

import pygame 
pygame.init ()
import numpy as np

LarguraTela = 1000
AlturaTela = 500

tela = pygame.display.set_mode ((LarguraTela, AlturaTela))

pygame.display.set_caption ("jogo")
walkRight = [pygame.image.load('D_01.png'), pygame.image.load('D_02.png'), pygame.image.load('D_03.png'), pygame.image.load('D_04.png'), pygame.image.load('D_05.png'), pygame.image.load('D_06.png'), pygame.image.load('D_07.png'), pygame.image.load('D_08.png'), pygame.image.load('D_09.png'), pygame.image.load('D_10.png'), pygame.image.load('D_11.png'), pygame.image.load('D_12.png'), pygame.image.load('D_13.png')]
walkLeft = [pygame.image.load('e_00.png'), pygame.image.load('e_01.png'), pygame.image.load('e_02.png'), pygame.image.load('e_03.png'), pygame.image.load('e_04.png'), pygame.image.load('e_05.png'), pygame.image.load('e_06.png'), pygame.image.load('e_07.png'), pygame.image.load('e_08.png'), pygame.image.load('e_09.png'), pygame.image.load('e_10.png'), pygame.image.load('e_11.png'), pygame.image.load('e_12.png')]
imagem_fundo1 = pygame.image.load('Ep-teste.png').convert()
char = [pygame.image.load('standing00.png'), pygame.image.load('standing01.png'), pygame.image.load('standing02.png'), pygame.image.load('standing03.png'), pygame.image.load('standing04.png'), pygame.image.load('standing05.png'), pygame.image.load('standing06.png'), pygame.image.load('standing07.png'), pygame.image.load('standing08.png'), pygame.image.load('standing09.png'), pygame.image.load('standing10.png'), pygame.image.load('standing11.png'), pygame.image.load('standing12.png')]
class Jogador(object):
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.h=h
        self.w=w


    def draw(self):
        pygame.draw.rect(tela,(255,255,255),pygame.Rect(self.x,self.y,self.w,self.h))
        
run=True
clock=pygame.time.Clock()
j1=Jogador(100,50,20,70)
j2=Jogador(900,50,20,70)
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    tela.fill((0,0,0))
    
    j1.draw()
    j2.draw()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: j2.y-=3
    if pressed[pygame.K_DOWN]: j2.y+=3
    
    if pressed[pygame.K_w]: j1.y-=3
    if pressed[pygame.K_s]: j1.y+=3
    #pygame.draw.rect(tela,(255,255,255),pygame.Rect(100,50,40,40))        
    pygame.display.update()
    clock.tick(60)