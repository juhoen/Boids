# coding: utf-8
#
# Copyright © 2016 Juho Enala
import numpy as np

# Number of boids
INDIVIDUALS = 100

# Map resolution
MAP_WIDTH = 500
MAP_HEIGHT = 500

# Max and min velocity
MIN_VELOCITY = 1.2
MAX_VELOCITY = 1.8

# Boid turning speed
TURNING_SPEED = 1.8

# Max FPS
FRAMES_PER_SECOND = 60

SEEING_RANGE = 95
PERSONAL_SPACE = 25
SEEING_ANGLE = 200

# Boids
ind_data = np.zeros([INDIVIDUALS, 4])

# Columns in boid matrix
POSX = 0
POSY = 1
VELO = 2
ORIE = 3



class Data():

    def __init__(self, separation, alignment, cohesion, seeing_range, personal_space, field_of_view):
        self.separation = separation
        self.alignment = alignment
        self.cohesion = cohesion
        self.seeing_range = seeing_range
        self.personal_space = personal_space
        self.field_of_view = field_of_view

    # Getters and setters
    def set_separation(self, value):
        self.separation = value

    def set_alignment(self, value):
        self.alignment = value

    def set_cohesion(self, value):
        self.cohesion = value

    def set_seeing_range(self, value):
        self.seeing_range = value

    def set_personal_space(self, value):
        self.personal_space = value

    def set_field_of_view(self, value):
        self.field_of_view = value

    def get_separation(self):
        return self.separation

    def get_alignment(self):
        return self.alignment

    def get_cohesion(self):
        return self.cohesion

    def get_seeing_range(self):
        return self.seeing_range

    def get_personal_space(self):
        return self.personal_space

    def get_field_of_view(self):
        return self.field_of_view

DEFAULT_SEPARATION = 1
DEFAULT_ALIGNMENT = 1
DEFAULT_COHESION = 1

# Both control window and simulation can interract with the same class and class attributes
setting_data = Data(DEFAULT_SEPARATION, DEFAULT_ALIGNMENT, DEFAULT_COHESION, SEEING_RANGE, PERSONAL_SPACE, SEEING_ANGLE)
