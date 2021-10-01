# Player module, the car.
import os, sys, pygame, math, maps
from pygame.locals import *
from random import randint
from loader import load_image

GRASS_SPEED = 0.715
GRASS_GREEN = 75
CENTER_X = -1
CENTER_Y = -1


# charkhesh car.
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def findspawn():
    x = randint(0, 9)
    y = randint(0, 9)
    while (maps.map_1[y][x] == 5):
        x = randint(0, 9)
        y = randint(0, 9)
    return x * 1000 + CENTER_X, y * 1000 + CENTER_Y


# tarif machine be onvan player.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('car_player.png')
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        CENTER_X = int(pygame.display.Info().current_w / 2)
        CENTER_Y = int(pygame.display.Info().current_h / 2)
        self.x = CENTER_X
        self.y = CENTER_Y
        self.rect.topleft = self.x, self.y
        self.x, self.y = findspawn()
        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 11.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.tracks = False

    # Reset the car.
    def reset(self):
        self.x = int(pygame.display.Info().current_w / 2)
        self.y = int(pygame.display.Info().current_h / 2)
        self.speed = 0.0
        self.dir = 0
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)
        self.rect.topleft = self.x, self.y
        self.x, self.y = findspawn()

    # khat bekesh..
    def emit_tracks(self):
        self.tracks = True

    # khat nakesh..
    def reset_tracks(self):
        self.tracks = False

    #age machine ro alafe khat bekesh.
    def grass(self, value):
        if value > GRASS_GREEN:
            if self.speed - self.deacceleration > GRASS_SPEED * 2:
                self.speed = self.speed - self.deacceleration * 2
                self.emit_tracks()

    # Push back on impact
    def impact(self):
        if self.speed > 0:
            self.speed = self.minspeed

    def soften(self):
        if self.speed > 0:
            self.speed -= self.softening
        if self.speed < 0:
            self.speed += self.softening

    # moshakhas kardan vehicle
    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration
            if self.speed < self.maxspeed / 3:
                self.emit_tracks()

    # namoshaKHAS.
    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed = self.speed - self.deacceleration
            self.emit_tracks()

    # HEDAYAT.
    def steerleft(self):
        self.dir = self.dir + self.steering
        if self.dir > 360:
            self.dir = 0
        if (self.speed > self.maxspeed / 2):
            self.emit_tracks()
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    # HEDAYAT.
    def steerright(self):
        self.dir = self.dir - self.steering
        if self.dir < 0:
            self.dir = 360
        if (self.speed > self.maxspeed / 2):
            self.emit_tracks()
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    # fix this function
    def update(self, last_x, last_y):
        self.x = self.x + self.speed * math.cos(math.radians(270 - self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270 - self.dir))
        self.reset_tracks()






