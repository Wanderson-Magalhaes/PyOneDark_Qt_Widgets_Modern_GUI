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

# PY LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyLeftMenu(QWidget):
    def __init__(
        self,
        parent = None,
        bg_color = "#1b1e23",
        bg_color_app = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2"
    ):
        super(PyLeftMenu, self).__init__()

        # SET PARENT
        self.parent = parent

        # SETUP WIDGETS
        self.setup_ui()

        self.button = QPushButton("teste")
        self.button_2 = QPushButton("teste")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_2)

        parent.setMinimumWidth(240)

    # SET APP LAYOUT
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self)
        self.left_menu_layout.setContentsMargins(0,0,0,0)

        # ADD BG
        self.bg = QFrame(self)
        self.bg.setStyleSheet("background: #CCC")

        # ADD LAYOUT
        self.layout = QVBoxLayout(self.bg)
        self.layout.setContentsMargins(0,0,0,0)        

        # ADD BG TO LAYOUT
        self.left_menu_layout.addWidget(self.bg)

        

        

