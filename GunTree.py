import pygame
from pygame.sprite import Sprite

class Gun(Sprite):    
    """Инициализация пушки"""
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("Study_Test_Img/ezhik2-128x79.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False
#        self.movetop = False
 #       self.movedown = False
    """Рисование пушки"""
    def output_gun(self):
        self.screen.blit(self.image, self.rect)    
    """Обновление позиции пушки"""
    def update_gun(self):
        if self.moveright and self.rect.right < self.screen_rect.right:
            self.rect.centerx+=5
        if self.moveleft and self.rect.left > self.screen_rect.left:
            self.rect.centerx-=5    
#        if self.movetop and self.rect.top > self.screen_rect.top:
 #           self.rect.centery-=1
  #      if self.movedown and self.rect.bottom < self.screen_rect.bottom:
   #         self.rect.centery+=1
    """размещает пушку внизу по центру"""
    def create_gun(self):
       self.center = self.screen_rect.centerx
