# coding: utf-8
#
# Copyright © 2016 Juho Enala

import time
from settings import *
from gui import mapgui, updategui
import pygame
import random
import numpy as np
import math


def engine(ind, map):

    screen = mapgui(ind_data)
    running = True

    # Simulation loop
    while running:
        start_time = time.time()

        # Fresh white screen
        screen.fill((252, 251, 251))

        for key, i in ind.items():
            # Boids in seeing range
            close_inds = i.get_close_inds(setting_data.get_seeing_range())

            # Too close boids
            too_close_inds = i.get_close_inds(setting_data.get_personal_space())

            # Get center point of individuals close by
            center = i.get_center(close_inds)

            # Get center point of too close individuals
            center_to_avoid = i.get_center(too_close_inds)

            # Get angles to the center points
            angle = i.get_angle(center)
            angle_to_avoid = i.get_angle(center_to_avoid)

            # Update boid orientation
            i.set_orientation(angle, angle_to_avoid + 180, close_inds)

            # Move boid
            i.move()

            # Update individual position in simulation screen
            updategui(ind_data[key], screen)

        # Render
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        end_time = time.time()

        # FPS limit
        sleep_time = (1 / FRAMES_PER_SECOND) - (end_time - start_time)
        if sleep_time > 0:
            time.sleep(sleep_time)


def get_random_position():
    posx = int(MAP_WIDTH * random.random())
    posy = int(MAP_HEIGHT * random.random())
    coordinates = (posx, posy)

    return coordinates


def get_random_velocity():
    return MIN_VELOCITY + (MAX_VELOCITY-MIN_VELOCITY) * random.random()


def get_random_orientation():
    orientation = 360 * random.random()
    return orientation


def turn_to(target_angle, own_angle):
    a = - target_angle + own_angle
    a = (a + 180) % 360 - 180
    if a < 0:
        own_angle = (own_angle + TURNING_SPEED) % 360
    elif a > 0:
        own_angle = own_angle - TURNING_SPEED
        if own_angle < 0:
            own_angle += 360

    return own_angle


def get_circular_mean(array_of_angles, id=None):
    ang1 = np.sum(np.cos(array_of_angles * np.pi / 180))
    ang2 = np.sum(np.sin(array_of_angles * np.pi / 180))
    ori_mean = np.arctan2(ang2, ang1) * 180 / np.pi
    if ori_mean == 0 and id is not None:
        return ind_data[id][ORIE]
    if ori_mean < 0:
        ori_mean += 360
    return ori_mean


def get_circular_mean2(angle_to_center, angle_mean_ori, angle_to_avoid):
    x = y = 0.
    angles = [angle_to_center, angle_mean_ori, angle_to_avoid]
    weights = [setting_data.get_cohesion(), setting_data.get_alignment(), setting_data.get_separation()]
    for angle, weight in zip(angles, weights):
        x += math.cos(math.radians(angle)) * weight
        y += math.sin(math.radians(angle)) * weight

    mean = math.degrees(math.atan2(y, x))
    if mean == 0:
        mean = None
    return mean


def get_final_angle(angle_own, angle_to_center, angle_to_avoid, angle_mean_ori):
    if np.isnan(angle_to_center):
        angle_to_center = angle_own
    if np.isnan(angle_to_avoid):
        angle_to_avoid = angle_own

    mean = get_circular_mean2(angle_to_center, angle_mean_ori, angle_to_avoid)
    if mean is None:
        mean = angle_own

    final_angle = turn_to(mean, angle_own)

    return final_angle
