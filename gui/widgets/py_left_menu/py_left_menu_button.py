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
        dark_one = "#1b1e23",
        dark_three = "#21252d",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        icon_path = "gui/images/svg_icons/icon_add_user.svg",
        icon_active_menu = "gui/images/svg_icons/active_menu.svg"
    ):
        super(PyLeftMenuButton, self).__init__()
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)

        # APP PATH
        app_path = os.path.abspath(os.getcwd())
        self._icon_path = os.path.normpath(os.path.join(app_path, icon_path))

        # PROPERTIES
        self._margin = margin
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._bg_one = bg_one
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_active = icon_color_active
        self._icon_set_color = self._icon_color
        self._icon_active_menu = icon_active_menu

    def paintEvent(self, event):
        # PAINTER
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        font = p.font()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        p.setFont(font)

        # RECTANGLES
        rect = QRect(4, 5, self.width(), self.height() - 10)
        rect_icon = QRect(0, 0, 50, self.height())
        rect_blue = QRect(4, 5, 20, self.height() - 10)
        rect_inside_active = QRect(7, 5, self.width(), self.height() - 10)
        rect_active_bar = QRect(self.width() - 5, 0, 5, self.height() - 10)
        rect_text = QRect(50, 0, self.width() - 50, self.height())

        # DRAW DEFAULT BG        
        p.setBrush(QColor(self._dark_one))
        p.drawRoundedRect(rect, 0, 0)

        # DRAW BG BLUE
        p.setBrush(QColor(self._context_color))
        p.drawRoundedRect(rect_blue, 8, 8)

        # BG INSIDE
        p.setBrush(QColor(self._bg_one))
        p.drawRoundedRect(rect_inside_active, 8, 8)

        # BG ACTIVE
        # p.setBrush(QColor(self._bg_one))
        # p.drawRect(rect_active_bar)

        # DRAW ICONS
        self.icon_paint(p, self._icon_path, rect_icon)

        # DRAW ACTIVE
        # APP PATH
        icon_path = self._icon_active_menu
        app_path = os.path.abspath(os.getcwd())
        icon_path = os.path.normpath(os.path.join(app_path, icon_path))
        self.icon_active(p, icon_path, self.width())

        # DRAW TEXT
        p.setPen(QColor(self._context_color))
        p.drawText(rect_text, Qt.AlignVCenter, self.text())

        p.end()

    # DRAW ICON WITH COLORS
    def icon_paint(self, qp, image, rect):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._icon_set_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()

    # DRAW ICON WITH COLORS
    def icon_active(self, qp, image, width):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._bg_one)
        qp.drawPixmap(width - 5, 0, icon)
        painter.end()

class _ActiveIcon(QLabel):
    def __init__(self, parent, tooltip):
        QLabel.__init__(self)

        # LABEL SETUP
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style_tooltip)
        self.setMaximumSize(10,60)
        self.setMinimumSize(10,60)
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

    
