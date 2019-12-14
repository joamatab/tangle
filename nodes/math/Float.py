from nodes.base_node import BaseNode
from core import socket_types as socket_types

from core.Constants import Colors

from ez_settings.ez_settings import EasySettingsBase


class Float(BaseNode):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, title_background_color=Colors.float, x=x, y=y)
        self.change_title("0.0")

        self.output_float = self.add_output(socket_types.FloatSocketType(self), "float")
        _, self.txt_number = self.add_label_float("number: ", number_changed_function=self.number_changed)

        EasySettingsBase().set_value("from float", 1)

    def number_changed(self):
        if self.txt_number.text() == "":
            self.output_float.set_value(0.0)
        try:
            self.output_float.set_value(float(self.txt_number.text()))
        except ValueError as err:
            self.output_float.set_value(0.0)

        self.set_dirty(True)
        self.compute()

    def compute(self):
        if self.is_dirty():
            super().compute()
            self.change_title(str(self.output_float.get_value()))
            self.set_dirty(False)

    def load(self, node_dict, x=None, y=None):
        super().load(node_dict, x=x, y=y)
        for socket_uuid, socket_dict in node_dict.get("sockets").items():
            self.txt_number.setText(str(socket_dict.get("value")))


