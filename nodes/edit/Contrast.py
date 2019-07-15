from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from nodes.image_node import ImageNode
import socket_types as socket_types

from functools import partial

from core.Constants import Colors
from PIL import Image, ImageQt, ImageOps, ImageEnhance, ImageFilter

class Contrast(ImageNode):
    def __init__(self, scene, x=0, y=0):
        super(Contrast, self).__init__(scene, title_background_color=Colors.contrast, x=x, y=y)
        self.change_title("contrast")

        self.input_image, self.output_image = self.add_input_output(socket_types.PictureSocketType(self), "image")

        self.add_label("Contrast amount")
        self.sld_contrast_amount = self.add_slider(0, 200, 100, changed_function=self.slider_changed, released_function=self.slider_released)

        self.set_auto_compute_on_connect(True)

    def slider_changed(self):
        self.compute()
        self.set_dirty(True)

    def slider_released(self):
        self.scene.refresh_network()


    def compute(self):
        if self.input_image.is_connected():
            self.input_image.fetch_connected_value()

            factor = self.sld_contrast_amount.value()

            contrasted = ImageEnhance.Contrast(self.input_image.get_value()).enhance(factor / 100)

            self.output_image.set_value(contrasted)

            contrasted_pixmap = ImageQt.toqpixmap(contrasted)
            self.set_pixmap(contrasted_pixmap)

            self.get_main_window().set_pixmap(contrasted_pixmap)
            self.set_dirty(False)
