import pygame

class Monster(pygame.sprite.Sprite):
            
    def __init__(self, screen):
        """Инициализируем и задаём начальную позицию"""    
        super(Monster, self).__init__()
        self.screen = screen
        self.image=pygame.image.load("Study_Test_Img/apple.png")
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    """вывод пришельца на экран"""
    def draw(self):
        self.screen.blit(self.image, self.rect)
    """перемещение пришельцев"""
    def update(self):
        self.y+=0.25
        self.rect.y=self.y
    
