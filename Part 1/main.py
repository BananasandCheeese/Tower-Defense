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
map_image = pg.image.load('levels/level.png').convert_alpha()
#enemies
enemy_image = pg.image.load('Part 1/assets/images/enemies/enemy_1.png').convert_alpha()



#create world
world = World(map_image)

# Create groups
enemy_group = pg.sprite.Group()

waypoints = [
  (100, 100),
  (400, 200),
  (400, 100),
  (200, 300),
]

enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

# Game loop
run = True
while run: 
  clock.tick(c.FPS)

  screen.fill("grey100")

  #draw level
  world.draw(screen)

  # Draw enemy path
  pg.draw.lines(screen, "grey0", False, waypoints)

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