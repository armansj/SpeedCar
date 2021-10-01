# dorbin chek mikonad ..............

# mode bazi inja tarif shode.

import pygame, maps
from pygame.locals import *
from loader import load_image
from random import randint

PENALTY_COOL = 180
FLAG_SCORE = 15
CRASH_PENALTY = -2
HALF_TILE = 500
FULL_TILE = 1000
COUNTDOWN_FULL = 3600
COUNTDOWN_EXTEND = 750


# in class baraye single object estefade mishe
#rad giri mikone score. It also manages the countdown timer.va timero neshon mide
class Finish(pygame.sprite.Sprite):
    # The player has collided and should pick the flag.
    def claim_flag(self):
        self.score += FLAG_SCORE
        self.timeleft += COUNTDOWN_EXTEND
        if self.timeleft > COUNTDOWN_FULL:
            self.timeleft = COUNTDOWN_FULL

    # The player has crashed into another vehicle, tasadof ba machine digar.
    def car_crash(self):
        if (self.penalty_cool == 0):
            self.score += CRASH_PENALTY
            self.penalty_cool = PENALTY_COOL

    # Find an adequate point to spawn flag.
    def generate_finish(self):
        x = randint(0, 9)
        y = randint(0, 9)
        while (maps.map_1[y][x] == 5):
            x = randint(0, 9)
            y = randint(0, 9)

        self.x = x * FULL_TILE + HALF_TILE
        self.y = y * FULL_TILE + HALF_TILE
        self.rect.topleft = self.x, self.y

    # Reset the state of the timer, score and respawn the flag.resatart kardan zaman
    def reset(self):
        self.timeleft = COUNTDOWN_FULL
        self.score = 0
        self.generate_finish()

    # Initialize.. yes.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('finish.png', False)
        self.rect = self.image.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.generate_finish()
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL

    # Update the timer and tekrar.
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y
        if (self.penalty_cool > 0):
            self.penalty_cool -= 1
        if (self.timeleft > 0):
            self.timeleft -= 1

