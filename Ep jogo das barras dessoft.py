# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:16:16 2019

@author: breno
"""
#git add . -- mandar todas as mudanÃ§as
#git commit -m ""
#git pull
#git push
import pygame
import math
import random

#parâmetros:
(width,height)=(1000,500)

screen=pygame.display.set_mode((width,height))
bgc=(255,255,255)


clock=pygame.time.Clock()

#criando os jogadores
class jogador(object):
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed=1
        
    def display(self):
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(self.x,self.y,self.w,self.h))
        
    def move(self,m):
        if m==1:
            self.y+=self.speed
        else: 
            self.y-=self.speed
    
    def bounce(self):
        if self.y>height:
            #print(True)
            self.y=0-self.h
            
        if self.y<0-self.h:
            self.y=height
            
class bola(object):
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.speed=1
        self.angle=converte_angulo(45)
    def display(self):
        pygame.draw.circle(screen,(0,0,0),(self.x,self.y),self.size)
        
    def move(self):
        self.x+=round(self.speed*(math.cos(self.angle)))
        self.y+=round(self.speed*(math.sin(self.angle)))
        
    def bounce(self):
        if self.y<=0+self.size:
            self.speed=-self.speed
            self.angle=random.uniform(converte_angulo(30),(60))
        if self.y>=500-self.size:
            self.speed=-self.speed
            self.angle=random.uniform(converte_angulo(30),(60))

def colisao(b,j):
    if j.x<=b.x<=j.x+j.w:
        b.speed=-b.speed
        
        
        

def converte_angulo(angulo):
    return angulo*math.pi/180           
run=True
j1=jogador(100,200,30,100)
j2=jogador(900,100,30,100)
ball=bola(500,250,10)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        j2.move(0)
    if pressed[pygame.K_w]:
        j1.move(0)
    if pressed[pygame.K_s]:
        j1.move(1)
    if pressed[pygame.K_DOWN]:
        j2.move(1)
    screen.fill(bgc)
    j1.display()
    j2.display()
    ball.display()
    ball.move()
    ball.bounce()
    colisao(ball,j1)
    j1.bounce()
    j2.bounce()
    #print(j1.x, j1.y)
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    
    

        