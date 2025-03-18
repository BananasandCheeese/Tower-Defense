import pygame as pg
from enemy import Enemy
import constants as c

# Initialise pygame
pg.init()

# Create clock
clock = pg.time.Clock()

# Create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

# Load images
enemy_image = pg.image.load('Part 1/assets/images/enemies/enemy_1.png').convert_alpha()

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