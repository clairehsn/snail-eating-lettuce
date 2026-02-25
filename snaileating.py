import pygame
import random

from pygame import *

largeur = 800
hauteur = 600

fond = pygame.image.load("esalade.png").convert()
def Fond_salade(fond):
    size=pygame.transform.scale(fond, (800,600))
    screen.blit(size, (0,0))

    
class Snail(pygame.sprite.Sprite):

    def __init__(self):
        super(Snail, self).__init__()
        self.surf = pygame.image.load("escargot.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largeur:
            self.rect.right = largeur
        if self.rect.top <= 0:
            self.rect.top = 0

pygame.init()
pygame.display.set_caption("Snail eating lettuce")


ecran = pygame.display.set_mode([largeur, hauteur])

snail = Snail()

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
      
    ecran.fill((0, 0, 0))
    Fond_salade(fond)

    touche_appuyee = pygame.key.get_pressed()

    snail.update(touche_appuyee)    
    pygame.display.flip()

    clock.tick(30)


pygame.time.delay(3000)
pygame.quit()
