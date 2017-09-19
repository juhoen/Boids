# coding: utf-8
#
# Copyright © 2016 Juho Enala

import pygame
from settings import *


def mapgui(map):
    global individual
    
    # Load assets
    individual = pygame.image.load("graphics/individual3.png")
    icon = pygame.image.load("graphics/logo.png")

    # Window settings
    pygame.display.set_caption("Boids")
    pygame.display.set_icon(icon)
    individual = pygame.transform.smoothscale(individual, (12, 12))
    screen = pygame.display.set_mode((MAP_WIDTH + 20, MAP_HEIGHT + 20))
    pygame.display.flip()

    screen.fill((251, 251, 251))

    return screen


def updategui(data, screen):
    rot_ind = pygame.transform.rotate(individual, data[ORIE])
    screen.blit(rot_ind, (data[POSX], data[POSY]))
