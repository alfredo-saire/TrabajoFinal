import pygame
from pygame.locals import *
from random import randint

pygame.init()
W = 800
H = 500
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Animaciones...')
f1 = pygame.image.load('images/fondo2.png')
f2 = pygame.image.load('images/fondo2.png')
p1 = [0,-f1.get_height()]
p2 = [0,0]
imgExpl = pygame.image.load('images/explosion_sheet.png')
NF = 1
NC = 12
WE = imgExpl.get_width() / NC
HE = imgExpl.get_height() / NF
xE = W / 2
yE = H / 2
salir = False
fActual = 0
cActual = 0
clock = pygame.time.Clock()
tcambio = pygame.time.get_ticks()
tcambioExplosion = pygame.time.get_ticks()
explosiones = []

while not salir:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == QUIT:
            salir = True
                
    dt = (pygame.time.get_ticks() - tcambio) / 10
    if dt >= 10:
        xne = randint(20,W-100)
        yne = randint(20,H-100)
        e = [xne, yne, 0, 0]
        explosiones.append(e)
        tcambio = pygame.time.get_ticks()

    screen.fill((0, 0, 0))
    screen.blit(f1, p1)
    screen.blit(f2,p2)
    p1[1] += 1
    p2[1] += 1
    if p1[1] >= H:
        p1[1] = -f1.get_height()
    if p2[1] >= H:
        p2[1] = -f2.get_height()
        
    for i in range(len(explosiones)):
        e = explosiones[i]
        frameActual = imgExpl.subsurface(e[3]*WE,e[2]*HE,WE,HE)
        screen.blit(frameActual, (e[0],e[1]))
    dt = (pygame.time.get_ticks() - tcambioExplosion) / 100
    if dt >= 0.2:
        tcambioExplosion = pygame.time.get_ticks()
        for i in range(len(explosiones)-1,-1,-1):
            if explosiones[i][3] < NC - 1:
                explosiones[i][3] += 1
            else:
                explosiones[i][3] = 0
                if explosiones[i][2] < NF-1:
                    explosiones[i][2] += 1
                else:
                    del explosiones[i]      
    pygame.display.flip()
pygame.quit()
                           
