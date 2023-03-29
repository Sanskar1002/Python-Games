import pygame as pg

# sprite is a default class of pygame having some functionalities
# library.module.class
class PLAYER(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("player.png").convert_alpha()

        # for changing size of image
        self.image = pg.transform.scale(self.image, (40, 80))

        # gives rectangle of the size of image
        self.rect = self.image.get_rect()

        # initial position of player
        self.rect.y = 700
        self.speed = 5

    def update(self, dt):
        # the keys which are pressed stored in key
        key = pg.key.get_pressed()

        if key[pg.K_UP]:
            self.rect.y -= self.speed * dt * 60
        elif key[pg.K_DOWN]:
            self.rect.y += self.speed * dt * 60
        elif key[pg.K_RIGHT]:
            self.rect.x += self.speed * dt * 60
        elif key[pg.K_LEFT]:
            self.rect.x -= self.speed * dt * 60
