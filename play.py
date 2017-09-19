# coding: utf-8
#
# Copyright © 2016 Juho Enala

from individual import Individual
import numpy as np
from settings import *
from gui import *
from map import Map
from engine import engine
from threading import Thread
import sys
from controls import QApplication, BoidControl
import time


# Create map
new_map = Map(MAP_WIDTH, MAP_HEIGHT)

# Create boids
ind = dict()
for i in range(INDIVIDUALS):
    ind[i] = Individual(i)

def open_gui():
    app = QApplication(sys.argv)
    ex = BoidControl()
    app.exec()

# Start simulation
Thread(target=engine, args=(ind, new_map)).start()

# Start control window
open_gui()
