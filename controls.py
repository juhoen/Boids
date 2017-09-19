# coding: utf-8
#
# Copyright © 2016 Juho Enala

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from settings import *


class BoidControl(QMainWindow):
    
    def __init__(self):
        super(BoidControl, self).__init__()

        self.value1 = QLabel(self)
        self.value1.setText("{}".format(setting_data.get_separation()))
        self.value1.setFixedWidth(40)
        self.value1.move(95, 20)

        self.value2 = QLabel(self)
        self.value2.setText(" {}".format(setting_data.get_alignment()))
        self.value2.setFixedWidth(40)
        self.value2.move(195, 20)

        self.value3 = QLabel(self)
        self.value3.setText("{}".format(setting_data.get_cohesion()))
        self.value3.setFixedWidth(40)
        self.value3.move(295, 20)

        self.value4 = QLabel(self)
        self.value4.setText("{}".format(setting_data.get_seeing_range()))
        self.value4.setFixedWidth(40)
        self.value4.move(395, 20)

        self.value5 = QLabel(self)
        self.value5.setText("{}".format(setting_data.get_personal_space()))
        self.value5.setFixedWidth(40)
        self.value5.move(495, 20)

        self.value6 = QLabel(self)
        self.value6.setText("{}".format(SEEING_ANGLE))
        self.value6.setFixedWidth(40)
        self.value6.move(595, 20)

        self.separation = QSlider(self)
        self.separation.setValue(setting_data.get_separation())
        self.separation.setFocusPolicy(Qt.NoFocus)
        self.separation.setGeometry(90, 50, 20, 150)
        self.separation.setTickPosition(QSlider.TicksRight)
        self.separation.setTickInterval(2)
        self.separation.valueChanged.connect(self.separation_change)
        self.separation.setMaximum(10)

        self.alignment = QSlider(self)
        self.alignment.setValue(setting_data.get_alignment())
        self.alignment.setFocusPolicy(Qt.NoFocus)
        self.alignment.setGeometry(190, 50, 20, 150)
        self.alignment.setTickPosition(QSlider.TicksRight)
        self.alignment.setTickInterval(2)
        self.alignment.valueChanged.connect(self.alignment_change)
        self.alignment.setMaximum(10)

        self.cohesion = QSlider(self)
        self.cohesion.setValue(setting_data.get_cohesion())
        self.cohesion.setFocusPolicy(Qt.NoFocus)
        self.cohesion.setGeometry(290, 50, 20, 150)
        self.cohesion.setTickPosition(QSlider.TicksRight)
        self.cohesion.setTickInterval(2)
        self.cohesion.valueChanged.connect(self.cohesion_change)
        self.cohesion.setMaximum(10)

        self.range1 = QSlider(self)
        self.range1.setFocusPolicy(Qt.NoFocus)
        self.range1.setGeometry(390, 50, 20, 150)
        self.range1.setTickPosition(QSlider.TicksRight)
        self.range1.setTickInterval(180)
        self.range1.valueChanged.connect(self.range1_change)
        self.range1.setMinimum(50)
        self.range1.setMaximum(500)
        self.range1.setValue(SEEING_RANGE)

        self.range2 = QSlider(self)
        self.range2.setFocusPolicy(Qt.NoFocus)
        self.range2.setGeometry(490, 50, 20, 150)
        self.range2.setTickPosition(QSlider.TicksRight)
        self.range2.setTickInterval(20)
        self.range2.valueChanged.connect(self.range2_change)
        self.range2.setMinimum(0)
        self.range2.setMaximum(100)
        self.range2.setValue(PERSONAL_SPACE)

        self.fov = QSlider(self)
        self.fov.setFocusPolicy(Qt.NoFocus)
        self.fov.setGeometry(590, 50, 20, 150)
        self.fov.setTickPosition(QSlider.TicksRight)
        self.fov.setTickInterval(60)
        self.fov.valueChanged.connect(self.fov_change)
        self.fov.setMaximum(360)
        self.fov.setValue(SEEING_ANGLE)

        self.reset = QPushButton(self)
        self.reset.setText("Reset")
        self.reset.setFixedWidth(80)
        self.reset.setFocusPolicy(Qt.NoFocus)
        self.reset.move(310, 250)
        self.reset.clicked.connect(self.reset_settings)

        text1 = QLabel(self)
        text1.setText("Separation")
        text1.move(65, 200)

        text2 = QLabel(self)
        text2.setText("Alignment")
        text2.move(165, 200)

        text3 = QLabel(self)
        text3.setText("Cohesion")
        text3.move(270, 200)

        text4 = QLabel(self)
        text4.setText("Seeing\n range")
        text4.move(380, 200)

        text5 = QLabel(self)
        text5.setText("Personal\n   space")
        text5.move(472, 200)

        text6 = QLabel(self)
        text6.setText("Field of\n   view")
        text6.move(573, 200)

        self.setFixedSize(700, 280)
        self.setWindowTitle('Boids Control')
        self.setWindowIcon(QIcon('graphics/logo.png'))
        self.show()

    def reset_settings(self):
        self.separation.setValue(DEFAULT_SEPARATION)
        self.alignment.setValue(DEFAULT_SEPARATION)
        self.cohesion.setValue(DEFAULT_COHESION)
        self.range1.setValue(SEEING_RANGE)
        self.range2.setValue(PERSONAL_SPACE)
        self.fov.setValue(SEEING_ANGLE)

    def separation_change(self):
        setting_data.set_separation(self.separation.value())
        self.value1.setText("{}".format(self.separation.value()))

    def alignment_change(self):
        setting_data.set_alignment(self.alignment.value())
        self.value2.setText("{}".format(self.alignment.value()))

    def cohesion_change(self):
        setting_data.set_cohesion(self.cohesion.value())
        self.value3.setText("{}".format(self.cohesion.value()))

    def range1_change(self):
        setting_data.set_seeing_range(self.range1.value())
        self.value4.setText("{}".format(self.range1.value()))

    def range2_change(self):
        setting_data.set_personal_space(self.range2.value())
        self.value5.setText("{}".format(self.range2.value()))

    def fov_change(self):
        setting_data.set_field_of_view(self.fov.value())
        self.value6.setText("{}".format(self.fov.value()))
