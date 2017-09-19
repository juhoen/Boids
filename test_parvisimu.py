# coding: utf-8
#
# Copyright © 2016 Juho Enala

import unittest
from individual import *
from settings import *
import numpy as np


class TestParvisimu(unittest.TestCase):

    def test_one(self):
        own_angle = 180
        target_angle = 200
        self.assertEqual(turn_to(target_angle, own_angle), own_angle + TURNING_SPEED)

        own_angle = 30
        target_angle = 350
        self.assertEqual(turn_to(target_angle, own_angle), own_angle - TURNING_SPEED)

        own_angle = 330
        target_angle = 10
        self.assertEqual(turn_to(target_angle, own_angle), own_angle + TURNING_SPEED)

    def test_two(self):
        angle1 = 50
        angle2 = 50
        angle3 = 50
        angle4 = 50
        array = np.array([angle1, angle2, angle3, angle4])
        self.assertEqual(get_circular_mean(array), 50)

        angle1 = 10
        angle2 = 10
        angle3 = 350
        angle4 = 350
        array = np.array([angle1, angle2, angle3, angle4])
        self.assertEqual(get_circular_mean(array) % 360, 0)

        angle1 = 10
        array = np.array([angle1])
        self.assertEqual(get_circular_mean(array) % 360, 10)

    def test_three(self):
        angle_own = 0
        angle_to_center = 0
        angle_to_avoid = 0
        angle_mean_ori = 0
        self.assertEqual(get_final_angle(angle_own, angle_to_center, angle_to_avoid, angle_mean_ori), 0)

        angle_own = 0
        angle_to_center = np.nan
        angle_to_avoid = np.nan
        angle_mean_ori = np.nan
        self.assertEqual(get_final_angle(angle_own, angle_to_center, angle_to_avoid, angle_mean_ori), 0)

    def test_four(self):
        angle1 = 50
        angle2 = 50
        angle3 = 50
        self.assertEqual(get_circular_mean2(angle1, angle2, angle3), 50)

        angle1 = 30
        angle2 = 0
        angle3 = 330
        self.assertEqual(get_circular_mean2(angle1, angle2, angle3) % 360.0, 360)

    def test_five(self):
        ind1 = Individual(0, (10, 0), 2, 0)
        self.assertEqual(Individual.get_center(ind1, ind_data), (10/INDIVIDUALS, 0))

        ind2 = Individual(1, (0, 0), 2, 0)
        ind3 = Individual(2, (20, 0), 2, 0)
        ind4 = Individual(3, (7, 0), 2, 0)
        ind5 = Individual(4, (8, 0), 2, 0)

        self.assertEqual(Individual.get_center(ind1, ind_data), (9*5/INDIVIDUALS, 0))

    def test_six(self):
        own_angle = 34.5
        ind1 = Individual(0, (500, 500), 2, own_angle)
        position = (600, 600)
        self.assertEqual(ind1.get_angle(position) % 360, 45)

        position = (500, 600)
        self.assertEqual(ind1.get_angle(position) % 360, 0)

        position = (600, 500)
        self.assertEqual(ind1.get_angle(position) % 360, 90)

        position = (400, 400)
        self.assertEqual(ind1.get_angle(position) % 360, 225)

        position = (600, 400)
        self.assertEqual(ind1.get_angle(position) % 360, 135)

        position = (400, 600)
        self.assertEqual(ind1.get_angle(position) % 360, 315)

        position = (500, 500)
        self.assertEqual(ind1.get_angle(position) % 360, own_angle)


if __name__ == '__main__':
    unittest.main()
