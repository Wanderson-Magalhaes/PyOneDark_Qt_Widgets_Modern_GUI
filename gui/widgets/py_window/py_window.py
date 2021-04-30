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
import sys

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class PyWindow(QWidget):
    def __init__(self, parent):
        super(PyWindow, self).__init__()

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # APP MARGINS LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.app_margins_layout = QVBoxLayout(self)
        self.app_margins_layout.setContentsMargins(0,0,0,0)
        self.app_margins_layout.setObjectName("app_margins_layout")

        # BG APP
        # ///////////////////////////////////////////////////////////////
        self.bg_app = QFrame(self)
        self.bg_app.setStyleSheet("background: #333")
        self.bg_app.setObjectName("bg_app")

        # ADD WIDGETS TO APP MARGINS LAUOUT
        # ///////////////////////////////////////////////////////////////
        self.app_margins_layout.addWidget(self.bg_app)
        
        