import pygame

class Bullet(pygame.sprite.Sprite):
    """Пуля в пушке"""
    def __init__(self,screen,gun):
        super(Bullet, self).__init__()
        self.screen=screen
        self.rect = pygame.Rect(0,0,64,12)
        self.color = 255,0,0
        self.speed = 9
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y=float(self.rect.y)
    """Перемещение пули"""   
    def update(self):
        self.y-=self.speed
        self.rect.y=self.y
    """Отрисовка пули"""
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
        
