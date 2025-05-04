import pygame as pg
from constants import *


class Bird(pg.sprite.Sprite):
    def __init__(self):
        super(Bird,self).__init__()

        self.load_animation()
        self.current_image = 0
        self.animation_right = self.playing_animation_right
        self.image = self.animation_right[self.current_image]

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)

        self.velocity_y = 0
        self.gravity = 0.05


        self.timer = pg.time.get_ticks()
        self.interval = 125


        # self.width = 64
        # self.height = 64

    def jump(self):
        self.velocity_y = -3

    def load_animation(self):
        num_images = 4
        tile_size = 16
        spritesheet = pg.image.load("Flappy Bird Assets/Player/StyleBird1/Bird1-2.png")
        self.playing_animation_right = []
        for i in range(num_images):
            x = i * tile_size
            y = 0
            rect = pg.Rect(x,y,tile_size,tile_size)
            image = spritesheet.subsurface(rect)
            image = pg.transform.scale_by(image, 5)
            self.playing_animation_right.append(image)

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y



        if pg.time.get_ticks() - self.timer > self.interval:
            self.current_image += 1
            if self.current_image >= len(self.animation_right):
                self.current_image = 0
            self.image = self.animation_right[self.current_image]
            self.timer = pg.time.get_ticks()

