from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from nodes.image_node import ImageNode
import socket_types as socket_types

from functools import partial

import PIL
from PIL import Image, ImageQt, ImageOps, ImageEnhance, ImageFilter

class Mirror(ImageNode):
    def __init__(self, scene, x=0, y=0):
        super(Mirror, self).__init__(scene, x=x, y=y)
        self.change_title("mirror")

        self.input_image = self.add_input(socket_types.PictureSocketType(self), "in")
        self.output_image = self.add_output(socket_types.PictureSocketType(self), "out")

        self.chk_horizontal = self.add_checkbox("Horizontal", change_checked_function=self.value_changed)
        self.chk_vertical = self.add_checkbox("Vertical", checked=False, change_checked_function=self.value_changed)

    def value_changed(self):
        self.set_dirty(True)
        self.scene.refresh_network()

    def compute(self):
        if self.input_image.is_connected():
            self.input_image.fetch_connected_value()

            mirrored = self.input_image.get_value()

            if self.chk_horizontal.isChecked():
                mirrored = ImageOps.mirror(mirrored)
            if self.chk_vertical.isChecked():
                mirrored = ImageOps.flip(mirrored)

            self.output_image.set_value(mirrored)

            mirrored_pixmap = ImageQt.toqpixmap(mirrored)
            self.set_pixmap(mirrored_pixmap)

            self.set_dirty(False)