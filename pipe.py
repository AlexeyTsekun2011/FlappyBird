from constants import *
import pygame as pg

class Pipe(pg.sprite.Sprite):
    def __init__(self,y):
        super(Pipe,self).__init__()
        spritesheet = pg.image.load("Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png")
        image = spritesheet.subsurface((0,0,32,80))#32,80
        # self.image = pg.transform.scale_by(image, 3.7)
        self.image = pg.transform.scale(image, (110,350))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y




    def update(self):
        self.rect.x -= 2.5
        if self.rect.right <= 0:
            self.kill()













