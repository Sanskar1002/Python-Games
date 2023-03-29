import pygame as pg
import sys
import time, random

from player import PLAYER
from enemy import ENEMY
from coin import COIN

pg.init()  # starting of pygame


class game:
    def __init__(self):  # constructor and self is a reference of object
        # for enemy
        self.score = 0
        self.x_pos = 0
        self.y_pos = 0
        self.count = 30

        # for coin
        self.coin_count = 0
        self.coin_x_pos = 0
        self.coin_y_pos = 0
        self.c_count = 50

        # window
        self.screen_width = 400
        self.screen_height = 800

        # game running
        self.is_game_over = False
        self.is_game_start = False

        # clock as an object to track time
        self.clock = pg.time.Clock()

        # variable to show a window on a screen
        self.win = pg.display.set_mode((self.screen_width, self.screen_height))

        # variable to show a road1 on window
        self.road1 = pg.image.load(
            "testroad.png"
        ).convert_alpha()  # for reducing load by converting image into pixels
        self.road1_rect = self.road1.get_rect()  # rectangle of road1 store in road_rect

        # variable to show a road2 on window
        self.road2 = pg.image.load(
            "testroad.png"
        ).convert_alpha()  # for reducing load by converting image into pixels
        self.road2_rect = self.road2.get_rect()  # rectangle of road2 store in road_rect

        # font for score
        self.font1 = pg.font.Font("arial 1.ttf", 30)
        self.score_text = self.font1.render("Score: 0", True, "blue", "white")
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.x = 10
        self.score_text_rect.y = 10

        # font for Game over
        self.font2 = pg.font.Font("arial 1.ttf", 48)
        self.game_over_text = self.font2.render(
            "Game Over", True, (255, 0, 0), (255, 255, 255)
        )
        self.game_over_text_rect = self.game_over_text.get_rect()
        self.game_over_text_rect.center = (
            self.screen_width // 2,
            self.screen_height // 2,
        )

        # font for Choose mode
        self.font3 = pg.font.Font("arial 1.ttf", 18)
        self.choice_text = self.font3.render(
            "Choose speed ", True, "#97FFFF", (0, 0, 0)
        )
        self.choice_text_rect = self.choice_text.get_rect()
        self.choice_text_rect.x = 240
        self.choice_text_rect.y = 50

        # font for easy mode
        self.font4 = pg.font.Font("arial 1.ttf", 12)
        self.choice1_text = self.font4.render(
            "1. Press 1 for slow speed ", True, "#97FFFF", (0, 0, 0)
        )
        self.choice1_text_rect = self.choice1_text.get_rect()
        self.choice1_text_rect.x = 240
        self.choice1_text_rect.y = 75

        # font for difficult
        self.font5 = pg.font.Font("arial 1.ttf", 12)
        self.choice2_text = self.font5.render(
            "3. Press 3 for high speed ", True, "#97FFFF", (0, 0, 0)
        )
        self.choice2_text_rect = self.choice2_text.get_rect()
        self.choice2_text_rect.x = 240
        self.choice2_text_rect.y = 105

        # font for reset
        self.font6 = pg.font.Font("arial 1.ttf", 18)
        self.reset_text = self.font6.render(
            "Press r for reset ", True, "#97FFFF", (0, 0, 0)
        )
        self.reset_text_rect = self.reset_text.get_rect()
        self.reset_text_rect.x = 10
        self.reset_text_rect.y = 50

        # font for exit
        self.font7 = pg.font.Font("arial 1.ttf", 18)
        self.exit_text = self.font7.render(
            "Press enter for exit ", True, "#97FFFF", (0, 0, 0)
        )
        self.exit_text_rect = self.exit_text.get_rect()
        self.exit_text_rect.x = 10
        self.exit_text_rect.y = 75

        # font for Welcome
        self.font8 = pg.font.Font("arial 1.ttf", 48)
        self.welcome_text = self.font8.render("WELCOME ", True, "blue", "white")
        self.welcome_text_rect = self.welcome_text.get_rect()
        self.welcome_text_rect.center = (
            self.screen_width // 2,
            self.screen_height // 2,
        )

        # font for start game
        self.font9 = pg.font.Font("arial 1.ttf", 24)
        self.start_text = self.font9.render(
            "Enter space to start the game ", True, "blue", "white"
        )
        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.center = (self.screen_width // 2, 450)

        # font for medium mode
        self.font10 = pg.font.Font("arial 1.ttf", 12)
        self.choice3_text = self.font10.render(
            "2. Press 2 for Medium speed ", True, "#97FFFF", (0, 0, 0)
        )
        self.choice3_text_rect = self.choice3_text.get_rect()
        self.choice3_text_rect.x = 240
        self.choice3_text_rect.y = 90

        # font for coin
        self.font11 = pg.font.Font("arial 1.ttf", 30)
        self.coin_text = self.font11.render("Coin: 0", True, "blue", "white")
        self.coin_text_rect = self.coin_text.get_rect()
        self.coin_text_rect.x = 280
        self.coin_text_rect.y = 10

        # initial position of road 1
        self.road1_rect.x = 0
        self.road1_rect.y = 0

        # initial position of road 2
        self.road2_rect.bottom = 0  # for keeping road2 just above road 1
        self.road2_rect.x = 0

        # speed for road
        self.road_speed = 5

        # frame rate
        self.target_fps = 120

        # object for player
        self.player = PLAYER()  # player is the object of PLAYER class

        # for enemy
        # list for enemy images
        self.enemy_image = []

        # loop for storing enemy image in enemy_image list
        for i in range(1, 5):
            img = pg.image.load(f"enemy{i}.png").convert_alpha()
            img = pg.transform.rotate(img, 180)
            img = pg.transform.scale(img, (40, 80))
            self.enemy_image.append(img)

        # variable for group
        self.enemy_group = pg.sprite.Group()

        # enemy generation
        self.enemy_generation(4, 0)

        # for coin
        # list for coin images
        self.coin_image = []

        # loop for storing coin image in coin_image list
        for i in range(1, 5):
            img = pg.image.load(f"coin{i}.png").convert_alpha()
            img = pg.transform.scale(img, (40, 40))
            self.coin_image.append(img)

        # variable for group
        self.coin_group = pg.sprite.Group()

        # coin generation
        self.coin_generation(4, 0)

        # method for game_loop
        self.game_loop()

    # definition of function for score updator
    def score_updater(self):
        self.score += 1
        self.score_text = self.font1.render(
            f"Score: {self.score}", True, "blue", "white"
        )

    # definition of function for coin point updator
    def coin_updator(self):
        self.coin_count += 1
        self.coin_text = self.font11.render(
            f"Coin: {self.coin_count}", True, "blue", "white"
        )

    # definition of function for gamr over
    def gameOver(self):
        self.is_game_over = True

    # definition of function for resetting game
    def reset(self):
        self.player.rect.y = 700
        self.score = 0
        self.coin_count = 0
        self.score_text = self.font1.render(
            f"Score: {self.score}", True, "blue", "white"
        )
        self.coin_text = self.font11.render(
            f"Coin: {self.coin_count}", True, "blue", "white"
        )

    # definition of function for game loop
    def game_loop(self):
        count = 0  # this variable decides the quantity of enemy generated
        c_count = 0  # this variable decides the quantity of coin generated

        # time before first frame change
        old_time = time.time()

        # infinite loop
        while True:
            # time after pervious frame change
            new_time = time.time()

            # time between two frame change
            dt = new_time - old_time
            old_time = new_time

            # loop for events done by user
            for event in pg.event.get():
                # closing the game
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_KP_ENTER
                ):
                    pg.quit()
                    sys.exit()

                # condition for functionalities in game
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_KP_1:
                        self.target_fps = 120

                    elif event.key == pg.K_KP_2:
                        self.target_fps = 180

                    elif event.key == pg.K_KP_3:
                        self.target_fps = 240

                    # for starting thw game
                    if event.key == pg.K_SPACE:
                        self.is_game_over = False
                        self.is_game_start = True

                    # for resettng
                    if event.key == pg.K_r:
                        self.reset()
                        self.is_game_start = False
                        self.is_game_over = False
                        self.check_collosion()

            if self.is_game_over == False:
                # for moving road 1 and 2 down in each frame
                self.road1_rect.y += int(self.road_speed * dt * self.target_fps)
                self.road2_rect.y += int(self.road_speed * dt * self.target_fps)

                # for updating player car position
                self.player.update(dt)

                # for updating enemy car position
                self.enemy_group.update(dt, self.target_fps)

                # for updating coin position
                self.coin_group.update(dt, self.target_fps)

                # for enemy
                if count == self.count:
                    last_x_pos = 10 + random.randint(0, 150)

                    # call for enemy generation
                    self.enemy_generation(1, last_x_pos)
                    count = 0
                else:
                    count += 1

                # for coin
                if c_count == self.c_count:
                    coin_last_x_pos = 10 + random.randint(0, 150)

                    # call for coin generation
                    self.coin_generation(1, coin_last_x_pos)
                    c_count = 0
                else:
                    c_count += 1

                # call for collosion checking between player enemy and coin
                self.check_collosion()

                # for making road one above other
                if self.road1_rect.y >= 800:
                    self.road1_rect.bottom = 0
                if self.road2_rect.y >= 800:
                    self.road2_rect.bottom = 0

            self.win.blit(self.road1, self.road1_rect)  # for showing road on window
            self.win.blit(self.road2, self.road2_rect)  # for showing road on window
            self.win.blit(
                self.player.image, self.player.rect
            )  # for showing player in window
            self.enemy_group.draw(
                self.win
            )  # the thing present in enemy_group will start showing on screen
            self.coin_group.draw(
                self.win
            )  # the thing present in coin_group will start showing on screen
            self.win.blit(
                self.score_text, self.score_text_rect
            )  # for showing score text on screen
            self.win.blit(
                self.coin_text, self.coin_text_rect
            )  # for showing coin text on screen
            self.win.blit(
                self.choice_text, self.choice_text_rect
            )  # for showing choose text mode on screen
            self.win.blit(
                self.choice1_text, self.choice1_text_rect
            )  # for showing slow speed text on screen
            self.win.blit(
                self.choice2_text, self.choice2_text_rect
            )  # for showing high speed text on screen
            self.win.blit(
                self.choice3_text, self.choice3_text_rect
            )  # for showing medium speed text on screen
            self.win.blit(
                self.reset_text, self.reset_text_rect
            )  # for showing reset text on screen
            self.win.blit(
                self.exit_text, self.exit_text_rect
            )  # for showing exit text on screen
            if self.is_game_over == True:
                self.win.blit(
                    self.game_over_text, self.game_over_text_rect
                )  # for showing game over text on screen
            if self.is_game_start == False:
                self.win.blit(
                    self.welcome_text, self.welcome_text_rect
                )  # for showing welcome text on screen
                self.win.blit(
                    self.start_text, self.start_text_rect
                )  # for showing enter space text text on screen

            # for updating the screen
            pg.display.update()

            # for delay the game by keeping 60 frames per sec
            self.clock.tick(60)

    # definition of function for checkind collosions
    def check_collosion(self):

        # between player and window
        if self.player.rect.x <= 0:
            self.player.rect.x = 0
        if self.player.rect.right > self.screen_width:
            self.player.rect.right = self.screen_width
        if self.player.rect.y <= 0:
            self.player.rect.y = 0
        if self.player.rect.bottom > self.screen_height:
            self.player.rect.bottom = self.screen_height

        # between player and enemy
        for enemy in self.enemy_group:
            if self.is_game_start == False and self.is_game_over == False:
                if enemy.rect.colliderect(self.player.rect):
                    pass
                if enemy.rect.y >= self.screen_height:
                    enemy.kill()
                    del enemy
            else:
                if enemy.rect.colliderect(self.player.rect):
                    self.gameOver()
                    break
                if enemy.rect.y >= self.screen_height:
                    enemy.kill()
                    del enemy
                    self.score_updater()

        # between player and coin
        for coin in self.coin_group:
            if self.is_game_start == False and self.is_game_over == False:
                if coin.rect.colliderect(self.player.rect):
                    pass
                if coin.rect.y >= self.screen_height:
                    coin.kill()
                    del coin
            else:
                if coin.rect.colliderect(self.player.rect):
                    coin.kill()
                    del coin
                    self.coin_updator()

    # definition of function for enemy generation
    def enemy_generation(self, count, last_x_pos):
        if self.is_game_start == True:
            for i in range(0, count):
                self.x_pos = last_x_pos + random.randint(
                    last_x_pos - 20, last_x_pos + 40
                )
                last_x_pos += 80
                self.y_pos = 10 - random.randint(0, 150)
                enemy = ENEMY(self.enemy_image, self.x_pos, self.y_pos)
                self.enemy_group.add(enemy)

    # definition of function for coin generation
    def coin_generation(self, c_count, coin_last_x_pos):
        if self.is_game_start == True:
            for i in range(0, c_count):
                self.coin_x_pos = coin_last_x_pos + random.randint(
                    coin_last_x_pos - 20, coin_last_x_pos + 40
                )
                coin_last_x_pos += 80
                self.coin_y_pos = 10 - random.randint(0, 150)
                coin = COIN(self.coin_image, self.coin_x_pos + 10, self.coin_y_pos + 10)
                self.coin_group.add(coin)


# object for game class
game_obj = game()
