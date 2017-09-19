# coding: utf-8
#
# Copyright © 2016 Juho Enala

import numpy
from engine import *
import math
from threading import Thread


class Individual:

    def __init__(self, id, pos=None, velocity=None, orientation=None):

        if pos is None:
            pos = get_random_position()
        if velocity is None:
            velocity = get_random_velocity()
        if orientation is None:
            orientation = get_random_orientation()

        self.id = id
        ind_data[self.id, POSX] = pos[0]                    # posx
        ind_data[self.id, POSY] = pos[1]                    # posy
        ind_data[self.id, VELO] = velocity                  # velocity
        ind_data[self.id, ORIE] = orientation               # orientation

    def get_close_inds(self, range):
        posx = ind_data[self.id, POSX]
        posy = ind_data[self.id, POSY]

        # Find close individuals
        close_inds = ind_data[np.ix_((posx - ind_data[:, POSX]) ** 2 + (posy - ind_data[:, POSY]) ** 2 <= range ** 2)]
        
        # Filter individuals in two batches
        close_inds_b1 = close_inds[np.arctan2(posx - close_inds[:, POSX], posy - close_inds[:, POSY]) * 180 / np.pi + 180 >= ind_data[self.id, ORIE] - SEEING_ANGLE/2]
        close_inds_b2 = close_inds[np.arctan2(posx - close_inds[:, POSX], posy - close_inds[:, POSY]) * 180 / np.pi + 180 <= ind_data[self.id, ORIE] + SEEING_ANGLE/2]
        
        # Concatenate and return close individuals
        return np.concatenate((close_inds_b1, close_inds_b2))

    def get_center(self, individuals):
        meanx = np.mean(individuals[:, POSX])
        meany = np.mean(individuals[:, POSY])
        return meanx, meany

    def get_angle(self, position):
        own_posx = ind_data[self.id, POSX]
        own_posy = ind_data[self.id, POSY]

        if position != (own_posx, own_posy):
            angle = math.atan2(own_posx - position[POSX], own_posy - position[POSY]) * 180 / math.pi + 180
            return angle

        return ind_data[self.id, ORIE]

    def set_orientation(self, angle, angle_to_avoid, close_inds):
        own_angle = ind_data[self.id, ORIE]
        mean_ori = get_circular_mean(close_inds[:, ORIE], self.id)

        final_angle = get_final_angle(own_angle, angle, angle_to_avoid, mean_ori)
        ind_data[self.id, ORIE] = final_angle

    def move(self):
        orientation = ind_data[self.id, ORIE]
        velocity = ind_data[self.id, VELO]

        velox = np.sin(orientation * np.pi / 180) * velocity
        veloy = np.cos(orientation * np.pi / 180) * velocity

        posx = ind_data[self.id, POSX] + velox
        posy = ind_data[self.id, POSY] + veloy

        if posx < 0:
            posx = MAP_WIDTH

        if posx > MAP_WIDTH:
            posx = 0

        if posy < 0:
            posy = MAP_HEIGHT

        if posy > MAP_HEIGHT:
            posy = 0

        ind_data[self.id, POSX] = posx
        ind_data[self.id, POSY] = posy


