import pygame
import numpy as np
from random import choice

pygame.init()

def Music():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load('level.mp3')
    pygame.mixer.music.play()

def SoundT():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play()

x = 160
y = 110
fimtel = 264

interva_pos = np.arange(0,250,1)
rand = choice(interva_pos)

run = 10

corDeFundo = (100,0,150)
altura = 296
largura = 264

fundo = pygame.image.load('background.png')
sprite = pygame.image.load('sprite.png')
spritefogo = pygame.image.load('spritefogo.png')

screen = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('janela')
ap_cdf = screen.fill((100,0,150))

Music()


running = True
while running == True:
    pygame.time.delay(50) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= run
    if comandos[pygame.K_DOWN]:
        y += run 
    if comandos[pygame.K_RIGHT]:
        x += run
    if comandos[pygame.K_LEFT]:
        x -= run
               
    if(x <= -10):
        x = 160
        SoundT()

    if(y <= -10):
        SoundT()
        y = 110
    


 

    screen.blit(fundo, (0,0))
    screen.blit(sprite, (x,y))

    pygame.display.update()


pygame.quit()

