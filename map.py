# coding: utf-8
#
# Copyright © 2016 Juho Enala

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        return self.width, self.height