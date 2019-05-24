#git add . -- mandar todas as mudanças
#git commit -m ""
#git pull
#git push
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
#bg2 = pygame.image.load('C:\\Users\\breno\\Documents\\fundo0 grande.png')
bg = imagem_fundo1
img0=pygame.image.load('fundo0 grande.png')
img1=pygame.image.load('fundo1 grande.png')
img2=pygame.image.load('fundo2 grande.png')
img3=pygame.image.load('fundo3 grande.png')
bg3=[img0,img1,img2,img3]

game_over=pygame.image.load('Game over.png')
'''def colisao_esquerda(player,inimigo):  #colisão esquerda 
    ladoX=player.x
    ladoX_Inimigo=inimigo.x+inimigo.width
    ladoY=player.y-player.height
    ladoY_inimigo=inimigo.y-inimigo.height
    j=range(ladoY,ladoY+player.height)
    hj=[]
    i=range(ladoY_inimigo,ladoY_inimigo+inimigo.height)
    hi=[]
    for a in i:
        hi.append([inimigo.x+inimigo.width,a])
    for a in j:
        hj.append([player.x,a])
    if player.x==inimigo.x and inter(hj,hi):
        return True'''
def inter(lista_j,lista_i):
    for i in lista_i:
        for j in lista_j:
            if i==j:
                return True
    return False
def pontos(obj):
    listaP=[]
    for i in np.arange(obj.x,obj.x+obj.width):
        listaP.append([i,obj.y])
    for i in np.arange(obj.x,obj.x+obj.width):
        listaP.append([i,obj.y-obj.height])
    for i in np.arange(obj.y,obj.y-obj.height):
        listaP.append([obj.x,i])
    for i in np.arange(obj.y,obj.y-obj.height):
        listaP.append([obj.x+obj.widht,i])
    return listaP
def colisao(player,inimigo):
    lista_p=pontos(player)
    lista_i=pontos(inimigo)
    c=inter(lista_p,lista_i)
    return c



class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.esquerda = False
        self.direita = False
        self.walkCount = 0
        self.parado = True
        self.hitbox = (self.x + 20, self.y + 5, 25, 55)

    def draw(self,tela):                    #movimento do jogador
        if self.walkCount + 1 >=9:
            self.walkCount = 0 
        if not(self.parado):
            if self.esquerda:
                tela.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.direita:
                tela.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.direita:
                tela.blit(walkRight[8], (self.x, self.y))
            else:
                tela.blit(walkLeft[8], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 5, 25, 55)
        pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 2)
        

    def toque (self):
        print ('toque')

class projectile(object): #pelotas (balas, pq o nome é estranho mesmo)
    def __init__(self, x, y, raio, cor, facing):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.facing = facing
        self.vel = 10 * facing
    #circulo        
    def draw(self,tela):
        pygame.draw.circle(tela, self.cor, (self.x,self.y), self.raio)


class fase(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.cor = cor
        self.width = width
        self.height = height
        self.facing = facing
        self.porta = (self.x + 25, self.y + 5, 25, 55)

    def draw(self,tela):
        self.porta = (self.x + 25, self.y + 5, 25, 55)
        l=lava(0,25)
        pygame.draw.rect(tela,(0,0,0),pygame.Rect(l.x,l.y,l.width,l.height))
        pygame.draw.rect(tela, (255, 255, 255), self.porta, 3 )

    def bg_change(bg):
        imagem_fundo1 = -1
        bg2 = 1

        pygame.display.update()

class inimigo(object):

    anda_direita = [pygame.image.load('inimigo0.png'), pygame.image.load('inimigo1.png'), pygame.image.load('inimigo2.png'), pygame.image.load('inimigo3.png'), pygame.image.load('inimigo4.png'), pygame.image.load('inimigo5.png')]           #colocar imagens do inimigo andando
    anda_esquerda = [pygame.image.load('inimigo20.png'), pygame.image.load('inimigo21.png'), pygame.image.load('inimigo22.png'), pygame.image.load('inimigo23.png'), pygame.image.load('inimigo24.png'), pygame.image.load('inimigo25.png')]


    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 10
        self.walkCount = 0

    def draw(self,tela):
        self.move()
        if self.walkCount + 1 <= 18: 
            self.walkCount = 0

        if self.vel > 0:
            tela.blit(self.anda_direita[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        else:
            tela.blit(self.anda_esquerda[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
            

    def move (self):
        if self.vel > 0:
            if self.x + self.vel < self.path [1]:       #anda pra direita
                self.x +=self.vel
            else:
                self.vel = self.vel * -1        #faz voltar para a esquerda
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]: #anda pra esquerda
                self.x += self.vel
            else:
                self.vel = self.vel * -1        #faz voltar para a direita
                self.walkCount = 0





class lava(object):
    def __init__(self,x,y,width=1000,height=25):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        
        
        
        
def DesenhoJanela(bg):
    tela.blit(bg, (0,0))
    pessoa.draw(tela)
    contra.draw(tela)
    for pelota in pelotas:
        pelota.draw(tela)

        
    pygame.display.update()

class barreira(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
                                                                                                                #loop principal

pessoa = player(5, 410, 64, 64)
contra = inimigo(100, 410, 64, 64, (LarguraTela - 100))
bar = barreira(100, 415, 50,100)
pelotas = []
run = True
clock = pygame.time.Clock()
contador=0
delay=0

while run:
   
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #colisão do player com o objeto
    

    for pelota in pelotas: 
        if pelota.x < LarguraTela and pelota.x > 0:   #anda se estiver dentro da area da tela
            pelota.x += pelota.vel
        else:
            pelotas.pop(pelotas.index(pelota))      #deleta a pelota se chegar no final da tela

    
    
    tecla = pygame.key.get_pressed()
    pygame.display.update()
    if tecla[pygame.K_SPACE]:
        pygame.key.set_repeat(100, 100)
        if pessoa.esquerda:
            facing = -1
        else:
            facing = 1
        if len(pelotas) < 5:
            pelotas.append(projectile(round(pessoa.x + pessoa.width //2), round(pessoa.y + pessoa.height //2), 3, (110,0,110), facing))
    
# os "and" no codigo fazem com que o personagem nao saia da tela
    
    if tecla[pygame.K_a] and pessoa.x > pessoa.vel:
        pessoa.x -= pessoa.vel
        pessoa.esquerda = True
        pessoa.direita = False
        pessoa.parado = False
    elif tecla[pygame.K_d] and pessoa.x < LarguraTela - pessoa.width - pessoa.vel:
        pessoa.x += pessoa.vel
        pessoa.esquerda = False
        pessoa.direita = True
        pessoa.parado = False
    else:
        pessoa.parado = True
        pessoa.walkCount = 0
  #pulo      
    if not(pessoa.isJump):
        if tecla[pygame.K_w]:
            #bg = bg2
            pessoa.isJump = True
            pessoa.direita = False
            pessoa.esquerda = False
            pessoa.walkCount = 0
            pygame.display.update()

    else:
        #funçao quadratica pra pular, com "neg" trazendo pra baixo
        if pessoa.jumpCount >= -10:
            neg = 1
            #por ser negativo, neg inverte a posicao e faz cair de volta
            if pessoa.jumpCount < 0:
                neg = -1
            if not colisao(pessoa,bar):
                pessoa.y -= (pessoa.jumpCount ** 2) * 0.3 * neg
                pessoa.jumpCount -= 1
            else:
                pessoa.jumpCount=0
            
        else:
            pessoa.isJump = False
            pessoa.jumpCount = 10
    
    #if colisao(pessoa,contra):
        #continue
        #tela.blit(game_over,(500-228,250-43))
        #pygame.display.update()
        #pygame.time.delay(600)
        #run=False
        
        
    if tecla[pygame.K_p]:
        bg = -1 ** (bg + 1)

        pygame.display.update()
            

    if contador>=4:
        contador=0
    DesenhoJanela(bg3[contador])
    if delay==60:
        contador+=1
        delay=0
    delay+=1
    #DesenhoJanela(bg)
    clock.tick(35)


pygame.quit()

