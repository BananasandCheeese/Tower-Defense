import pygame as pg

class World():
    def __init__(self, map_image):
        self.map_image = map_image

    def draw(self, screen): 
        screen.blit(self.image, (0, 0))
        