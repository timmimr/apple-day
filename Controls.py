import pygame
import sys
from bullet import Bullet
from monster import Monster
import time
import stats
"""Обработка событий"""
def events(screen,gun,bullets,stats):    
    for event in pygame.event.get():
        """Закрытие окна по нажатию на крестик"""
        if event.type == pygame.QUIT:
            sys.exit()        
        if event.type == pygame.KEYDOWN:
            """открыть или закрыть меню"""
            if event.key == pygame.K_ESCAPE:
                if stats.run_game==False:
                    stats.run_game=True
                else:
                    stats.run_game=False
            """ Стрельба"""
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen,gun)
                bullets.add(new_bullet)
            """Передвижение пушки удерживаемой клавишей"""    
            if event.key == pygame.K_a:
                gun.moveleft=True     
            if event.key == pygame.K_d:
                gun.moveright=True
#            if event.key == pygame.K_w:
 #               gun.movetop=True
  #          if event.key == pygame.K_s:
   #             gun.movedown=True
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_a:
                gun.moveleft=False     
             if event.key == pygame.K_d:
                gun.moveright=False
#             if event.key == pygame.K_w:
 #               gun.movetop=False
  #           if event.key == pygame.K_s:
   #             gun.movedown=False
"""Обновление экрана"""                
def screen_update(bg_color, screen,stats,sc, gun, apples, bullets):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output_gun()
    apples.draw(screen)
    pygame.display.flip()
"""Обновление расположения пуль"""
def update_bullets(screen, stats, sc, apples, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,apples,True,True)
    if collisions:
        for apples in collisions.values():
            stats.score+=10*len(apples)
        sc.image_score()
        check_high_score(stats,sc)
        sc.image_guns_life()
    if len(apples)==0:
        bullets.empty()
        create_army(screen,apples)
"""Создание армии монстров"""    
def create_army(screen, apples):
    apple=Monster(screen)
    apple_width = apple.rect.width
    apple_height = apple.rect.height
    number_apple_y=int((512-128-2*apple_height)/apple_height)
    number_apple_x=int((1024-9*apple_width)/apple_width)
    for row_number in range(number_apple_y):
        for apple_number in range(number_apple_x):
            apple = Monster(screen)
            apple.x=apple_width+apple_width*apple_number
            apple.y=apple_height+apple_height*row_number
            apple.rect.x=apple.x
            apple.rect.y=apple.rect.height+apple.rect.height*row_number
            apples.add(apple)
"""обновляет позицию монстров"""
def update_apples(stats, screen, sc, gun,apples,bullets):
    apples.update()
    if pygame.sprite.spritecollideany(gun,apples):
        gun_kill(stats, screen, sc, gun,apples,bullets)
    check_border_apples(stats,screen,sc,gun,apples,bullets)
"""Столкновение пушки и армии"""
def gun_kill(stats,screen,sc, gun,apples,bullets):
    if stats.guns_left>0:
        stats.guns_left-=1
        apples.empty()
        sc.image_guns_life()
        create_army(screen,apples)
        time.sleep(1)
        gun.create_gun()
    else:
        stats.run_game=False
        sys.exit()
"""проверка, добралась ли армия до края экрана"""
def check_border_apples(stats,screen, sc,gun,apples,bullets):
    screen_rect=screen.get_rect()
    for apple in apples.sprites():
        if apple.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun,apples,bullets)
            break
"""проверка новых рекордов"""
def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open("config.txt","w") as f:
            f.write(str(stats.high_score))
