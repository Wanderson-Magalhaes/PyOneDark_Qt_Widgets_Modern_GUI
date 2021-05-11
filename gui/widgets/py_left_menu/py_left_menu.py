# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT BUTTON
# ///////////////////////////////////////////////////////////////
from . py_left_menu_button import PyLeftMenuButton

# PY LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyLeftMenu(QWidget):
    def __init__(
        self,
        parent = None,
        dark_one = "#1b1e23",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        duration_time = 500,
        radius = 8
    ):
        super(PyLeftMenu, self).__init__()

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
        self._bg_dark_one = dark_one,
        self._bg_one = bg_one,
        self._icon_color = icon_color,
        self._icon_color_hover = icon_color_hover,
        self._icon_color_pressed = icon_color_pressed,
        self._icon_color_active = icon_color_active,
        self._context_color = context_color
        self._duration_time = duration_time
        self._radius = radius

        # SET PARENT
        self.parent = parent

        # SETUP WIDGETS
        self.setup_ui()

        # SET BG COLOR
        self.bg.setStyleSheet(f"background: {dark_one}; border-radius: {radius};")

        self.button = PyLeftMenuButton("Add user menu")
        self.button.clicked.connect(lambda: self.size_change())
        self.button_2 = QPushButton("teste")
        self.button_3 = PyLeftMenuButton("Teste menu", icon_path="gui/images/svg_icons/icon_settings.svg")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_2)
        self.layout.addWidget(self.button_3)

        

    def size_change(self):
        self.animation = QPropertyAnimation(self.parent, b"minimumWidth")
        self.animation.stop()
        if self.width() == 50:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(240)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(50)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._duration_time)      
        self.animation.start()

    # SET APP LAYOUT
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self)
        self.left_menu_layout.setContentsMargins(0,0,0,0)

        # ADD BG
        self.bg = QFrame(self)

        # ADD LAYOUT
        self.layout = QVBoxLayout(self.bg)
        self.layout.setContentsMargins(0,0,0,0)        

        # ADD BG TO LAYOUT
        self.left_menu_layout.addWidget(self.bg)

        

        

