import pygame as pg
import random

class COIN(pg.sprite.Sprite):
    def __init__(self,coin_image,x_pos,y_pos):
        super().__init__()
        index = random.randint(0,3)
        self.image=coin_image[index]
        self.rect = self.image.get_rect()
        self.rect.y = y_pos
        self.rect.x = x_pos
        self.speed = 3
    def update(self,dt,target_fps):
        self.rect.y += self.speed*dt*target_fps