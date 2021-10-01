
#Media loader class.
#Loads images.

import os, sys, pygame
from pygame.locals import *

#Load an image. :)
def load_image(file, transparent = True):
    print("Loading " + file + " ..")
    fullname = os.path.join('media', file)
    image = pygame.image.load(fullname)
    if transparent == True:
        image = image.convert()
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image
