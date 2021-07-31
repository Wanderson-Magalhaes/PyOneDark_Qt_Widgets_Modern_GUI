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

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# PY ICON WITH CUSTOM COLORS
# ///////////////////////////////////////////////////////////////
class PyIcon(QWidget):
    def __init__(
        self,
        icon_path,
        icon_color
    ):
        super().__init__()

        # PROPERTIES
        self._icon_path = icon_path
        self._icon_color = icon_color

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        # LAYOUT
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        # LABEL
        self.icon = QLabel()
        self.icon.setAlignment(Qt.AlignCenter)
        
        # PAINTER
        self.set_icon(self._icon_path, self._icon_color)

        # ADD TO LAYOUT
        self.layout.addWidget(self.icon)

    def set_icon(self, icon_path, icon_color = None):
        # GET COLOR
        color = ""
        if icon_color != None:
            color = icon_color
        else:
            color = self._icon_color

        # PAINTER / PIXMAP
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)       
        painter.end()

        # SET PIXMAP
        self.icon.setPixmap(icon)

