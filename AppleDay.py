import pygame
import sys
from GunTree import Gun
from pygame.sprite import Group
import Controls
from stats import Stats
from score import Scores
import time
def run():
    pygame.init()
    screen=pygame.display.set_mode((1024,512))
    pygame.display.set_caption("ЯБЛОЁЖ")
    bg_color=(0,0,255)
    gun=Gun(screen)
    apples=Group()
    Controls.create_army(screen,apples)
    bullets=Group()
    stats = Stats()
    sc=Scores(screen,stats)
    while True:
        Controls.events(screen, gun, bullets,stats)
        if stats.run_game:
            gun.update_gun()
            Controls.screen_update(bg_color, screen, stats, sc, gun, apples, bullets)
            Controls.update_bullets(screen, stats,sc, apples, bullets)
            Controls.update_apples(stats, screen,sc, gun,apples,bullets)
        else:
            
        
run()
