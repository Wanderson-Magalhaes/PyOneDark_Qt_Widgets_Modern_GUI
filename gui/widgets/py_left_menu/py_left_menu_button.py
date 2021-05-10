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

# IMPORT COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# TOOLTIP / LABEL StyleSheet
style_tooltip = """ 
QLabel {		
	background-color: #0b0b0c;	
	color: rgb(230, 230, 230);
	padding-left: 10px;
	padding-right: 10px;
	border-radius: 17px;
    border: 1px solid #2f3032;
    border-left: 3px solid #bdff00;
    font: 800 9pt "Segoe UI";
}
"""

# CUSTOM LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyLeftMenuButton(QPushButton):
    def __init__(
        self,
        text,
        margin = 4,
        bg_one_color = "#2c313c"
    ):
        super(PyLeftMenuButton, self).__init__()
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setMaximumHeight(40)
        self.setMinimumHeight(40)

        # PROPERTIES
        self._margin = margin
        self._bg_one_color = bg_one_color

    def paintEvent(self, event):
        # PAINTER
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)

        # RECTANGLES
        rect = QRect(0, 0, self.width(), self.height())
        rect_inside = QRect(
            self._margin,
            self._margin,
            self.width() - (self._margin * 2),
            self.height() - (self._margin * 2)
        )

        # DRAW BG        
        p.setBrush(QColor(self._bg_one_color))
        p.drawRoundedRect(rect, 0, 0)

        # BG INSIDE
        p.setBrush(QColor("red"))
        p.drawRoundedRect(rect_inside, self._margin, self._margin)

        p.end()

class _ToolTip(QLabel):
    def __init__(self, parent, tooltip):
        QLabel.__init__(self)

        # LABEL SETUP
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style_tooltip)
        self.setMinimumHeight(36)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(self.shadow)

        # SET OPACITY
        self.opacity = QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(0.85)
        self.setGraphicsEffect(self.opacity)

    
