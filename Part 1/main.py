import pygame as pg
from enemy import Enemy
import constants as c

#initialise pygame
pg.mixer.init()
pg.init()
pg.mixer.quit()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

#load images
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

#create groups
enemy_group = pg.sprite.Group()

enemy = Enemy((200,300), enemy_image)
enemy_group.add(enemy)

#game loop
run = True
while run: 
   
   clock.tick(c.FPS)

   #draw groups
   enemy_group.draw(screen)

   #event handler
   for event in pg.event.get():
    #quit program
    if event.type == pg.QUIT:
      run = False

pg.quit()          