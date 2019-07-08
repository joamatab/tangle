from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from nodes.image_node import ImageNode
import socket_types as socket_types

import logging
logging.basicConfig(level=logging.INFO)

import nv_utils.qt_utils as qutils

from PIL import Image, ImageQt, ImageOps, ImageEnhance, ImageFilter

class SizeReduce(ImageNode):
    def __init__(self, scene, x=0, y=0):
        super(SizeReduce, self).__init__(scene, x=x, y=y)
        self.change_title("resize")

        self.input_image = self.add_input(socket_types.PictureSocketType(self), "in")
        self.output_image = self.add_output(socket_types.PictureSocketType(self), "out")
        self.size = self.add_output(socket_types.TupleSocketType(self), "size")

        percentage_list = ["0", "25", "50", "75"]

        self.cb_percentage = self.add_label_combobox("Reduce by %", percentage_list, changed_function=self.value_changed)

    def value_changed(self):
        self.set_dirty(True)
        self.scene.refresh_network()

    def compute(self):
        if self.input_image.is_connected():
            print("computing reduce size")
            self.input_image.fetch_connected_value()

            width, height = self.input_image.get_value().size

            new_width = int((width * (100 - int(self.cb_percentage.currentText()))) / 100)
            new_height = int((height * (100 - int(self.cb_percentage.currentText()))) / 100)

            resized = self.input_image.get_value().resize((new_width, new_height), Image.ANTIALIAS)
            self.output_image.set_value(resized)

            resized_pixmap = ImageQt.toqpixmap(resized)
            self.set_pixmap(resized_pixmap)

            self.size.set_value(resized.size)

            self.set_dirty(False)