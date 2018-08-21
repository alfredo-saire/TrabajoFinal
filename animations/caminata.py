import pygame
from pygame.locals import *
from time import *

def iniciar():
    global W, H, screen, imagen, clock, speed
    W = 800
    H = 600
    speed = 1
    
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Animacion de SpriteSheets')
    imagen = pygame.sprite.Sprite()
    imagen.image = pygame.image.load('images/caminata.png')
    imagen.rect  = imagen.image.get_rect()
    imagen.rect.top = 0
    imagen.rect.left = -imagen.rect.width
    imagen.nroFrames = 8
    imagen.actualFrame = -1
    imagen.anchoFrame = imagen.rect.width / imagen.nroFrames

    clock = pygame.time.Clock()

def obtenerImagen():
    imagen.actualFrame = (imagen.actualFrame + 1) % imagen.nroFrames
    surface = imagen.image.subsurface(imagen.actualFrame*imagen.anchoFrame,0,imagen.anchoFrame, imagen.rect.height)
    return surface

def main():
    global tiempo
    iniciar()
    salir = False
    posx = -imagen.anchoFrame
    while not salir:
        time = clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir = True
                
        img = obtenerImagen()
        posx += 10
        if posx > 900:
            posx = -100
        screen.fill((255,255,255))
        screen.blit(img, (posx, 0))
        screen.blit(pygame.transform.flip(img,True, False),(800 - posx - imagen.anchoFrame,0))
        pygame.display.flip()
        sleep(0.1)

if __name__ == '__main__' :
    pygame.init()
    main()
    pygame.quit()
