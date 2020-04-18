import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from functools import partial
import uuid

import logging
logging.basicConfig(level=logging.INFO)

from core.Node import Node
from core.SignalEmitter import SignalEmitter
from core.Constants import Colors, ss

import nv_utils.qt_utils as qt_utils

SCRIPT_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
UI_PATH = os.path.join(SCRIPT_FOLDER, "ui")
SETTINGS_PATH = os.path.join(SCRIPT_FOLDER, "settings", "tangle_settings.json")
ICONS_PATH = os.path.join(SCRIPT_FOLDER, "ui", "icons")
NODE_FOLDER = os.path.join(SCRIPT_FOLDER, "nodes")

class BaseNode(Node):
    def __init__(self, scene, title="unnamed_node", title_background_color=Colors.node_selected_border ,x=0, y=0):
        super().__init__(scene, title, title_background_color, x, y)
        self.scene = scene
        self.__x = x
        self.__y = y

        self.__module_path = None

        self.__widget = QWidget()
        self.__layout = QVBoxLayout()

        self.__is_dirty = True
        self.__auto_compute_on_connect = True

        self.__widget.setLayout(self.__layout)

        self.lbl_node_type = self.add_label(str(type(self).__name__), align_center=True)
        self.lbl_node_type.setStyleSheet(ss.bold_12pt)
        self.lbl_uuid = self.add_label(str(self.get_uuid()), align_center=True)
        self.lbl_uuid.setStyleSheet(ss.bold_9pt)

        icon_layout = QHBoxLayout()
        self.__layout.addLayout(icon_layout)
        self.lbl_icon = self.add_label("", align_center=True)
        self.lbl_icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.lbl_icon.setFixedHeight(128)
        self.set_icon()
        icon_layout.addWidget(self.lbl_icon)

        self.add_horizontal_line()
        self.add_spacer()

    def set_icon(self):
        if self.has_icon():
            icon_pixmap = self.get_icon()
            self.lbl_icon.setVisible(True)
            self.lbl_icon.setPixmap(icon_pixmap.scaled(48, 48, transformMode=Qt.SmoothTransformation))
            self.add_icon_circle_pixmap(icon_pixmap)
        else:
            self.lbl_icon.setVisible(False)
            return

    def has_icon(self):
        if not self.get_icon(as_pixmap=False) == "":
            return True
        return False

    def get_icon(self, as_pixmap=True):
        icon_path = os.path.join(ICONS_PATH, os.path.basename(str(type(self).__name__))) + ".png"
        if as_pixmap:
            if os.path.isfile(icon_path):
                return QPixmap(icon_path)
            return QPixmap()
        else:
            if os.path.isfile(icon_path):
                return icon_path
            return ""

    def refresh(self):
        pass

    def set_module_path(self, module_path):
        self.__module_path = module_path

    def get_module_path(self):
        return self.__module_path

    def set_auto_compute_on_connect(self, value):
        self.__auto_compute_on_connect = value

    def get_auto_compute_on_connect(self):
        return self.__auto_compute_on_connect

    def compute(self):
        self.compute_connected_nodes()

    def set_dirty(self, is_dirty, emit=False):
        self.__is_dirty = is_dirty

    def is_dirty(self):
        return self.__is_dirty

    def compute_connected_nodes(self, output_socket=None):
        if output_socket is None:
            for node in self.get_connected_output_nodes():
                node.set_dirty(True)
                node.compute()
        else:
            for connected_node in [socket.get_node() for socket in output_socket.get_connected_sockets()]:
                connected_node.set_dirty(True)
                connected_node.compute()

    def get_ui(self):
        return self.__widget

    def get_x(self):
        return self.scenePos().x()

    def get_y(self):
        return self.scenePos().y()

    def get_main_window(self):
        return self.scene.get_main_window()

    def add_button(self, button_text, clicked_function):
        button = QPushButton(button_text)
        button.clicked.connect(clicked_function)
        self.__layout.addWidget(button)

        return button

    def add_label(self, label_text, align_center=False):
        label = QLabel(label_text)
        if align_center:
            label.setAlignment(Qt.AlignCenter)
        self.__layout.addWidget(label)

        return label

    def add_horizontal_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        self.__layout.addWidget(line)

    def add_spacer(self, width=10, height=20):
        spacer = QSpacerItem(10, 20)
        self.__layout.addSpacerItem(spacer)

        return spacer

    def add_text_line(self, text="", text_changed_function=None):
        txt_line = QLineEdit()

        if text_changed_function is not None:
            txt_line.textChanged.connect(text_changed_function)

        self.__layout.addWidget(txt_line)

        return txt_line

    def add_label_text_button(self, label_text, button_text, clicked_function):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        txt_line = QLineEdit()
        button = QPushButton(button_text)

        button.clicked.connect(clicked_function)

        layout.addWidget(label)
        layout.addWidget(txt_line)
        layout.addWidget(button)

        self.__layout.addLayout(layout)

        return[label, txt_line, button]

    def add_label_text(self, label_text, txt_text="", text_changed_function=None):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        txt_line = QLineEdit(str(txt_text))

        layout.addWidget(label)
        layout.addWidget(txt_line)

        if text_changed_function is not None:
            txt_line.textChanged.connect(text_changed_function)

        self.__layout.addLayout(layout)

        return[label, txt_line]

    def add_label_float(self, label_text, number=0.000, number_changed_function=None):
        layout = QHBoxLayout()
        label = QLabel(label_text)

        txt_float = QLineEdit(str(number))

        layout.addWidget(label)
        layout.addWidget(txt_float)

        if number_changed_function is not None:
            txt_float.textChanged.connect(number_changed_function)

        self.__layout.addLayout(layout)

        return[label, txt_float]

    def add_checkbox(self, label, checked=True, change_checked_function=None):
        checkbox = QCheckBox(label)
        checkbox.setChecked(checked)

        if change_checked_function is not None:
            checkbox.stateChanged.connect(change_checked_function)

        self.__layout.addWidget(checkbox)

        return checkbox

    def add_slider(self, minimum, maximum, start, changed_function=None, released_function=None):
        def set_label_text(slider, label):
            label.setText(str(slider.value()))

        layout = QHBoxLayout()
        slider = QSlider()
        slider.setMinimum(minimum)
        slider.setMaximum(maximum)
        slider.setValue(start)
        slider.setOrientation(Qt.Horizontal)

        label = QLabel(str(slider.value()))

        if changed_function is not None:
            slider.sliderMoved.connect(changed_function)

        if released_function is not None:
            slider.sliderReleased.connect(released_function)

        slider.valueChanged.connect(partial(set_label_text, slider, label))

        layout.addWidget(slider)
        layout.addWidget(label)

        self.__layout.addLayout(layout)

        return slider

    def add_combobox(self, items=[], changed_function=None):
        combobox = QComboBox()
        qt_utils.cb.add_items(combobox, items=items)

        if changed_function is not None:
            combobox.currentIndexChanged.connect(changed_function)

        self.__layout.addWidget(combobox)

        return combobox

    def add_label_combobox(self, label_text, items=[], changed_function=None):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        combobox = QComboBox()
        qt_utils.cb.add_items(combobox, items=items)

        layout.addWidget(label)
        layout.addWidget(combobox)

        if changed_function is not None:
            combobox.currentIndexChanged.connect(changed_function)

        self.__layout.addLayout(layout)

        return combobox

    def add_spinbox(self, value=0, changed_function=None):
        spin_number = QDoubleSpinBox()
        spin_number.setKeyboardTracking(False)
        spin_number.setDecimals(3)
        spin_number.setMaximum(float("inf"))
        spin_number.setMinimum(float("-inf"))
        spin_number.setButtonSymbols(QAbstractSpinBox.NoButtons)

        spin_number.valueChanged.connect(changed_function)

        self.__layout.addWidget(spin_number)

        return spin_number

    def add_label_spinbox(self, label_text, value=0, changed_function=None):
        layout = QHBoxLayout()

        label = QLabel(label_text)

        spin_number = QDoubleSpinBox()
        spin_number.setKeyboardTracking(False)
        spin_number.setDecimals(3)
        spin_number.setMaximum(float("inf"))
        spin_number.setMinimum(float("-inf"))

        layout.addWidget(label)
        layout.addWidget(spin_number)

        spin_number.valueChanged.connect(changed_function)

        self.__layout.addLayout(layout)

        return spin_number

    def add_list_widget(self, multiselect=False, custom_context_menu_function=None, selection_changed_function=None):
        layout = QHBoxLayout()

        list_widget = QListWidget()
        if multiselect:
            list_widget.selectionMode(QAbstractItemView.ExtendedSelection)

        if selection_changed_function is not None:
            list_widget.currentItemChanged.connect(selection_changed_function)

        if custom_context_menu_function is not None:
            list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
            list_widget.customContextMenuRequested.connect(custom_context_menu_function)

        layout.addWidget(list_widget)
        self.__layout.addLayout(layout)

        return list_widget

    def add_custom_widget(self, widget):
        self.__layout.addWidget(widget)

        return widget

    def save(self, save_value=True):
        node_dict = {}
        node_dict["sockets"] = {}
        for socket in self.get_all_sockets():
            node_dict["sockets"][socket.get_uuid(as_string=True)] = socket.save(save_value=save_value)

        for socket in self.get_connected_output_sockets():
            node_dict["sockets"][socket.get_uuid(as_string=True)]["connections"] = {}
            for index, socket_connection in enumerate(socket.get_connections()):
                connected_input_socket = socket_connection.get_input_socket()
                node_dict["sockets"][socket.get_uuid(as_string=True)]["connections"][index] = [socket.get_uuid(as_string=True), connected_input_socket.get_uuid(as_string=True)]

        node_dict["node_specific_params"] = {}
        node_dict["uuid"] = self.get_uuid(as_string=True)
        node_dict["x"] = self.get_x()
        node_dict["y"] = self.get_y()
        node_dict["module_path"] = self.get_module_path()
        node_dict["class_name"] = self.get_module_path().split(".")[-1]
        node_dict["module_name"] = self.get_module_path().split(".")[-2]

        return node_dict

    def duplicate(self):
        node_dict = self.save()
        scene_dict = {}
        scene_dict["nodes"] = {}
        scene_dict["nodes"][node_dict.get("uuid")] = node_dict
        self.scene.open_network(scene_dict=scene_dict, with_values=True, with_connections=False, is_duplicate=True)
        return node_dict

    def load(self, node_dict, is_duplicate=False, x=None, y=None):
        if x is not None:
            x_pos = x
        else:
            x_pos = node_dict.get("x")
        if y is not None:
            y_pos = y
        else:
            y_pos = node_dict.get("y")

        self.setPos(x_pos, y_pos)
        if is_duplicate:
            self.set_uuid(uuid.uuid4())
        else:
            self.set_uuid(node_dict.get("uuid"))

    def error(self, socket, text):
        logging.error("Node: %s\nSocket: %s\n%s" % (self.name, socket.name, text))

    def warning(self, socket, text):
        logging.warning("Node: %s\nSocket: %s\n%s" % (self.name, socket.name, text))

    def info(self, socket, text):
        logging.info("Node: %s\nSocket: %s\n%s" % (self.name, socket.name, text))

    def __str__(self):
        return "%s - %s" % (self.__class__.__name__, self.get_uuid(as_string=True))



