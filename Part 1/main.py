import pygame as pg
import json
from enemy import Enemy
from world import World
from turret import Turret
import constants as c

# Initialise pygame
pg.init()

# Create clock
clock = pg.time.Clock()

# Create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

# Load images
#map
map_image = pg.image.load('Part 1/assets/levels/level.png').convert_alpha()
#individual turret image for map cursor
cursor_turret = pg.image.load('Part 1/assets/images/turrets/cursor_turret.png').convert_alpha()
#enemies
enemy_image = pg.image.load('Part 1/assets/images/enemies/enemy_1.png').convert_alpha()

#load json data for level
with open('Part 1/assets/levels/level.tmj') as file:
  world_data = json.load(file)

def create_turret(mouse_pos):
   mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
   mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
   #calculate the sequential number of the tile
   mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
   #check if that tile is grass
   if world.tile_map[mouse_tile_num] == 7:
    #check that there isn't already a turret there
    space_is_free = True
    for turret in turret_group:
      if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
        space_is_free = False
        #if it is a free space then create a turret
    if space_is_free:
      new_turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
      turret_group.add(new_turret)

#create world
world = World(world_data, map_image)
world.process_data()

# Create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

# Game loop
run = True
while run: 
  clock.tick(c.FPS)

  screen.fill("grey100")

  #draw level
  world.draw(screen)

  # Update groups
  enemy_group.update()

  # Draw groups
  enemy_group.draw(screen)
  turret_group.draw(screen)

  # Event handler
  for event in pg.event.get():
    # Quit program
    if event.type == pg.QUIT:
      run = False
    #Mouse click
    if event.type ==  pg.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = pg.mouse.get_pos()
      #check if mouse is on the game area
      if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
        create_turret(mouse_pos)

  # Update display
  pg.display.flip()

pg.quit()          