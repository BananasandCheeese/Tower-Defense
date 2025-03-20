import pygame as pg
import json
from enemy import Enemy
from world import World
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
#enemies
enemy_image = pg.image.load('Part 1/assets/images/enemies/enemy_1.png').convert_alpha()

#load json data for level
with open('Part 1/assets/levels/level.tmj') as file:
  world_data = json.load(file)


#create world
world = World(world_data, map_image)
world.process_data()

# Create groups
enemy_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

# Game loop
run = True
while run: 
  clock.tick(c.FPS)

  screen.fill("grey100")

  #draw level
  world.draw(screen)

  # Draw enemy path
  pg.draw.lines(screen, "grey0", False, world.waypoints)

  # Update groups
  enemy_group.update()

  # Draw groups
  enemy_group.draw(screen)

  # Event handler
  for event in pg.event.get():
    # Quit program
    if event.type == pg.QUIT:
      run = False

  # Update display
  pg.display.flip()

pg.quit()          