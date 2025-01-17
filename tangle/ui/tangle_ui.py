# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tangle.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tangle_window(object):
    def setupUi(self, tangle_window):
        if not tangle_window.objectName():
            tangle_window.setObjectName(u"tangle_window")
        tangle_window.resize(1294, 916)
        icon = QIcon()
        icon.addFile(u"icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        tangle_window.setWindowIcon(icon)
        tangle_window.setStyleSheet(u"")
        self.action_exit = QAction(tangle_window)
        self.action_exit.setObjectName(u"action_exit")
        self.action_settings = QAction(tangle_window)
        self.action_settings.setObjectName(u"action_settings")
        self.action_reload_nodes = QAction(tangle_window)
        self.action_reload_nodes.setObjectName(u"action_reload_nodes")
        self.action_show_image_viewer = QAction(tangle_window)
        self.action_show_image_viewer.setObjectName(u"action_show_image_viewer")
        self.action_show_image_viewer.setShortcutContext(Qt.ApplicationShortcut)
        self.action_clear_scene = QAction(tangle_window)
        self.action_clear_scene.setObjectName(u"action_clear_scene")
        self.action_clear_scene.setShortcutContext(Qt.ApplicationShortcut)
        self.action_duplicate_nodes = QAction(tangle_window)
        self.action_duplicate_nodes.setObjectName(u"action_duplicate_nodes")
        self.action_duplicate_nodes.setShortcutContext(Qt.ApplicationShortcut)
        self.action_delete_nodes = QAction(tangle_window)
        self.action_delete_nodes.setObjectName(u"action_delete_nodes")
        self.action_delete_nodes.setShortcutContext(Qt.ApplicationShortcut)
        self.action_save_scene = QAction(tangle_window)
        self.action_save_scene.setObjectName(u"action_save_scene")
        self.action_save_scene.setShortcutContext(Qt.ApplicationShortcut)
        self.action_load = QAction(tangle_window)
        self.action_load.setObjectName(u"action_load")
        self.action_load.setShortcutContext(Qt.ApplicationShortcut)
        self.action_save_selected_nodes = QAction(tangle_window)
        self.action_save_selected_nodes.setObjectName(u"action_save_selected_nodes")
        self.action_save_selected_nodes.setShortcutContext(Qt.ApplicationShortcut)
        self.action_recompute_entire_network = QAction(tangle_window)
        self.action_recompute_entire_network.setObjectName(u"action_recompute_entire_network")
        self.action_group_ungroup_nodes = QAction(tangle_window)
        self.action_group_ungroup_nodes.setObjectName(u"action_group_ungroup_nodes")
        self.action_group_ungroup_nodes.setShortcutContext(Qt.ApplicationShortcut)
        self.action_about = QAction(tangle_window)
        self.action_about.setObjectName(u"action_about")
        self.action_align_selected_nodes_vertically = QAction(tangle_window)
        self.action_align_selected_nodes_vertically.setObjectName(u"action_align_selected_nodes_vertically")
        self.action_align_selected_nodes_vertically.setShortcutContext(Qt.ApplicationShortcut)
        self.action_align_selected_nodes_horizontally = QAction(tangle_window)
        self.action_align_selected_nodes_horizontally.setObjectName(u"action_align_selected_nodes_horizontally")
        self.action_align_selected_nodes_horizontally.setShortcutContext(Qt.ApplicationShortcut)
        self.actionsdf = QAction(tangle_window)
        self.actionsdf.setObjectName(u"actionsdf")
        self.action_show_graph_viewer = QAction(tangle_window)
        self.action_show_graph_viewer.setObjectName(u"action_show_graph_viewer")
        self.action_show_graph_viewer.setShortcutContext(Qt.ApplicationShortcut)
        self.action_show_graph_viewer_date = QAction(tangle_window)
        self.action_show_graph_viewer_date.setObjectName(u"action_show_graph_viewer_date")
        self.action_show_graph_viewer_date.setShortcutContext(Qt.ApplicationShortcut)
        self.action_generate_node_database = QAction(tangle_window)
        self.action_generate_node_database.setObjectName(u"action_generate_node_database")
        self.action_show_about = QAction(tangle_window)
        self.action_show_about.setObjectName(u"action_show_about")
        self.action_import_nodes_from_file = QAction(tangle_window)
        self.action_import_nodes_from_file.setObjectName(u"action_import_nodes_from_file")
        self.centralwidget = QWidget(tangle_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontal_splitter = QSplitter(self.centralwidget)
        self.horizontal_splitter.setObjectName(u"horizontal_splitter")
        self.horizontal_splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.horizontal_splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.main_vertical_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.main_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_splitter.addWidget(self.verticalLayoutWidget)
        self.vertical_splitter = QSplitter(self.horizontal_splitter)
        self.vertical_splitter.setObjectName(u"vertical_splitter")
        self.vertical_splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.vertical_splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.node_tree_layout = QVBoxLayout(self.layoutWidget)
        self.node_tree_layout.setObjectName(u"node_tree_layout")
        self.node_tree_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_splitter.addWidget(self.layoutWidget)
        self.scrollArea = QScrollArea(self.vertical_splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 446, 136))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.values_layout = QVBoxLayout()
        self.values_layout.setSpacing(1)
        self.values_layout.setObjectName(u"values_layout")
        self.values_layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.gridLayout.addLayout(self.values_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.vertical_splitter.addWidget(self.scrollArea)
        self.layoutWidget_2 = QWidget(self.vertical_splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.log_layout = QVBoxLayout(self.layoutWidget_2)
        self.log_layout.setObjectName(u"log_layout")
        self.log_layout.setContentsMargins(0, 0, 0, 0)
        self.tree_log = QTreeWidget(self.layoutWidget_2)
        self.tree_log.setObjectName(u"tree_log")

        self.log_layout.addWidget(self.tree_log)

        self.vertical_splitter.addWidget(self.layoutWidget_2)
        self.horizontal_splitter.addWidget(self.vertical_splitter)

        self.gridLayout_2.addWidget(self.horizontal_splitter, 0, 0, 1, 1)

        tangle_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tangle_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1294, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuGraph = QMenu(self.menuView)
        self.menuGraph.setObjectName(u"menuGraph")
        self.menuScene = QMenu(self.menubar)
        self.menuScene.setObjectName(u"menuScene")
        self.menuScene.setTearOffEnabled(False)
        self.menuNodes = QMenu(self.menubar)
        self.menuNodes.setObjectName(u"menuNodes")
        tangle_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tangle_window)
        self.statusbar.setObjectName(u"statusbar")
        tangle_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScene.menuAction())
        self.menubar.addAction(self.menuNodes.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.action_show_about)
        self.menuFile.addAction(self.action_exit)
        self.menuEdit.addAction(self.action_settings)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_reload_nodes)
        self.menuEdit.addAction(self.action_generate_node_database)
        self.menuEdit.addSeparator()
        self.menuView.addAction(self.action_show_image_viewer)
        self.menuView.addAction(self.menuGraph.menuAction())
        self.menuGraph.addAction(self.action_show_graph_viewer)
        self.menuGraph.addAction(self.action_show_graph_viewer_date)
        self.menuScene.addAction(self.action_save_scene)
        self.menuScene.addAction(self.action_load)
        self.menuScene.addSeparator()
        self.menuScene.addAction(self.action_clear_scene)
        self.menuScene.addSeparator()
        self.menuScene.addAction(self.action_recompute_entire_network)
        self.menuNodes.addAction(self.action_save_selected_nodes)
        self.menuNodes.addAction(self.action_duplicate_nodes)
        self.menuNodes.addAction(self.action_group_ungroup_nodes)
        self.menuNodes.addAction(self.action_import_nodes_from_file)
        self.menuNodes.addSeparator()
        self.menuNodes.addAction(self.action_align_selected_nodes_horizontally)
        self.menuNodes.addAction(self.action_align_selected_nodes_vertically)
        self.menuNodes.addSeparator()
        self.menuNodes.addAction(self.action_delete_nodes)

        self.retranslateUi(tangle_window)

        QMetaObject.connectSlotsByName(tangle_window)
    # setupUi

    def retranslateUi(self, tangle_window):
        tangle_window.setWindowTitle(QCoreApplication.translate("tangle_window", u"Tangle by Niels Vaes", None))
        self.action_exit.setText(QCoreApplication.translate("tangle_window", u"Exit", None))
        self.action_settings.setText(QCoreApplication.translate("tangle_window", u"Settings", None))
        self.action_reload_nodes.setText(QCoreApplication.translate("tangle_window", u"Reload Node Browser", None))
        self.action_show_image_viewer.setText(QCoreApplication.translate("tangle_window", u"Image", None))
#if QT_CONFIG(shortcut)
        self.action_show_image_viewer.setShortcut(QCoreApplication.translate("tangle_window", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.action_clear_scene.setText(QCoreApplication.translate("tangle_window", u"Clear scene", None))
#if QT_CONFIG(shortcut)
        self.action_clear_scene.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.action_duplicate_nodes.setText(QCoreApplication.translate("tangle_window", u"Duplicate nodes", None))
#if QT_CONFIG(shortcut)
        self.action_duplicate_nodes.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.action_delete_nodes.setText(QCoreApplication.translate("tangle_window", u"Delete nodes", None))
#if QT_CONFIG(shortcut)
        self.action_delete_nodes.setShortcut(QCoreApplication.translate("tangle_window", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_scene.setText(QCoreApplication.translate("tangle_window", u"Save scene...", None))
#if QT_CONFIG(shortcut)
        self.action_save_scene.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_load.setText(QCoreApplication.translate("tangle_window", u"Load...", None))
#if QT_CONFIG(shortcut)
        self.action_load.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_selected_nodes.setText(QCoreApplication.translate("tangle_window", u"Save selected nodes...", None))
#if QT_CONFIG(shortcut)
        self.action_save_selected_nodes.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_recompute_entire_network.setText(QCoreApplication.translate("tangle_window", u"Re-compute entire network", None))
        self.action_group_ungroup_nodes.setText(QCoreApplication.translate("tangle_window", u"Group/ungroup selected nodes", None))
#if QT_CONFIG(shortcut)
        self.action_group_ungroup_nodes.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("tangle_window", u"About...", None))
        self.action_align_selected_nodes_vertically.setText(QCoreApplication.translate("tangle_window", u"Align selected nodes vertically", None))
#if QT_CONFIG(shortcut)
        self.action_align_selected_nodes_vertically.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+Left", None))
#endif // QT_CONFIG(shortcut)
        self.action_align_selected_nodes_horizontally.setText(QCoreApplication.translate("tangle_window", u"Align selected nodes horizontally", None))
#if QT_CONFIG(shortcut)
        self.action_align_selected_nodes_horizontally.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionsdf.setText(QCoreApplication.translate("tangle_window", u"sdf", None))
        self.action_show_graph_viewer.setText(QCoreApplication.translate("tangle_window", u"Float Graph", None))
#if QT_CONFIG(shortcut)
        self.action_show_graph_viewer.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+F6", None))
#endif // QT_CONFIG(shortcut)
        self.action_show_graph_viewer_date.setText(QCoreApplication.translate("tangle_window", u"Date Graph", None))
#if QT_CONFIG(shortcut)
        self.action_show_graph_viewer_date.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+F7", None))
#endif // QT_CONFIG(shortcut)
        self.action_generate_node_database.setText(QCoreApplication.translate("tangle_window", u"Generate Node Database", None))
        self.action_show_about.setText(QCoreApplication.translate("tangle_window", u"About...", None))
        self.action_import_nodes_from_file.setText(QCoreApplication.translate("tangle_window", u"Import nodes from file...", None))
#if QT_CONFIG(shortcut)
        self.action_import_nodes_from_file.setShortcut(QCoreApplication.translate("tangle_window", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        ___qtreewidgetitem = self.tree_log.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("tangle_window", u"Log", None));
        self.menuFile.setTitle(QCoreApplication.translate("tangle_window", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("tangle_window", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("tangle_window", u"Viewers", None))
        self.menuGraph.setTitle(QCoreApplication.translate("tangle_window", u"Graph", None))
        self.menuScene.setTitle(QCoreApplication.translate("tangle_window", u"Scene", None))
        self.menuNodes.setTitle(QCoreApplication.translate("tangle_window", u"Nodes", None))
    # retranslateUi

