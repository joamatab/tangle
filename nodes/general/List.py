from nodes.base_node import BaseNode
from core import socket_types as socket_types

from core.Constants import Colors

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ez_settings.ez_settings import EasySettingsBase

import nv_utils.qt_utils as qutils
import nv_utils.utils as utils


class List(BaseNode):
    def __init__(self, scene, x=0, y=0):
        super().__init__(scene, title_background_color=Colors.lists, x=x, y=y)
        self.items = []

        self.update_title()

        self.output_list = self.add_output(socket_types.ListSocketType(self), "list")
        self.lw_list = self.add_list_widget(custom_context_menu_function=self.show_context_menu)
        _, self.txt_item = self.add_label_text("add item: ")

        self.txt_item.returnPressed.connect(self.return_pressed)

    def show_context_menu(self):
        root_menu = QMenu(self.lw_list)
        root_menu.addAction("Remove selected from list", self.remove_selected_from_list)

        root_menu.popup(QCursor.pos())

    def remove_selected_from_list(self):
        for item in self.lw_list.selectedItems():
            self.items.remove(utils.try_parse(item.text()))
        qutils.remove_items_from_list_widget(self.lw_list, selected=True)


    def return_pressed(self):
        self.items.append(utils.try_parse(self.txt_item.text()))

        qutils.add_items_to_list_widget(self.lw_list, [str(item) for item in self.items], duplicates_allowed=True, clear=True)
        self.output_list.set_value(self.items)

        self.set_dirty(True)
        self.txt_item.clear()
        self.update_title()
        self.compute()

    def update_title(self):
        self.change_title(f"list - {len(self.items)}")

    def compute(self):
        if self.is_dirty():
            super().compute()

    def load(self, node_dict, is_duplicate=False, x=None, y=None):
        super().load(node_dict, is_duplicate=is_duplicate, x=x, y=y)
        for socket_uuid, socket_dict in node_dict.get("sockets").items():
            if socket_dict.get("label") == self.output_list.get_name():
                self.items = socket_dict.get("value")
                qutils.add_items_to_list_widget(self.lw_list, [str(item) for item in self.items],
                                                duplicates_allowed=True, clear=True)
                self.update_title()
                self.output_list.set_value(self.items)
