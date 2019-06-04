0# -*- coding: utf-8 -*-
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

#criando a bola
class particle(object):
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

#criando os jogadores
class player(object):
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

def colisao(b,j):
    if j.x<=b.x<=j.x+j.w:
        b.speed=-b.speed
        
        
        
#converte pra radianos
def converte_angulo(angulo):
    return angulo*math.pi/180

#converte pra graus:
def conv_angulo(angulo):
    return angulo*180/math.pi



def colisao_direita(par,pla):
    #colisoes do lado direito da tela
    dx=par.x(pla.x+pla.width)
    dyt=par.x-pla.y
    dyb= par.y-(pla.y+pla.height)
    if dx<=0:
        if dyt>=0 or dyb>=0:
            par.speed=-par.speed
            par.angle=random.uniform(math.pi/2,3*math.pi/2)
            
# trata as colisões do lado esquerdo da tela
def colisao_esquerda(par,pla):
    dx=par.y-pla.x
    dyt=par.y-pla.y
    dyb=par.y-(pla.y-pla.height)
    if dx>=0:
        if dyt>=0 or dyb<=0:
            par.speed=-par.speed
            par.angle= random.uniform(math.pi/2,3*math.pi/2)
  #trata todas as colisões:          
def colisao_player_particle(player,particle):
    rtop=player.y
    rleft=player.x
    rright, rbottom= rleft+player.width/2, rtop+player.height/2
    cleft,ctop= particle.x-particle.size, particle.y-particle.size
    cright, cbottom= particle.x+particle.size, particle.y+particle.size
    
    
    if rright<cleft or rleft>cright or rbottom<ctop or rtop>cbottom:
        return False 
    
    
    for x in (rleft,rleft+player.width):
        for y in (rtop, rtop+player.height):
            if math.hypot(x-particle.x,y-particle.y)<=particle.size:
                return True
            
    
    if rleft<=particle.x <= rright and rtop <= particle.y <= rbottom:
        return True
    
    return False
 #Creation Zone:              
run=True
j1=player(100,200,30,100)
j2=player(900,100,30,100)
bola=particle(500,250,15)
#loop principal:
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
    bola.display()
    bola.move()
    bola.bounce()
    colisao(bola,j1)
    j1.bounce()
    j2.bounce()
    #print(j1.x, j1.y)
    result=particle.bounce()
   
    
    #Winning condition:
    if result and particle.x <500:
        print("player 2 ganhou")
        run=False
    elif result and particle.x>500:
        print("player 1 ganhou")
        
    #display zone:
    j1.display()
    j2.display()
    particle.display()
    
    #Colision Zone:
    a=colisao_player_particle(j1,particle)
    b=colisao_player_particle(j2,particle)
    
    if a:
        print(a)
        particle.x=j1.x+j2.width+1
        particle.speed=-particle.speed
        particle.angle= random.uniform(math.pi/2, 3*math.pi/2)
    if b:
        print(b)
        particle.x=j2.x-1
        particle.speed=-particle.speed
        particle.angle= random.uniformm(math.pi/2, 3*math.pi/2)
    

    
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    
    

        