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

# PY TITLE BUTTON
# ///////////////////////////////////////////////////////////////
class PyTitleButton(QPushButton):
    def __init__(
        self,
        tooltip_text = "",
        width = 30,
        height = 30,
        radius = 8,
        bg_color = "#343b48",
        bg_color_hover = "#3c4454",
        bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        icon_path = "no_icon.svg",
        is_active = False
    ):
        super(PyTitleButton, self).__init__()
        
        # SET DEFAULT PARAMETERS
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)

        # PROPERTIES
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed        
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        # Set Parameters
        self._set_bg_color = bg_color
        self._set_icon_path = icon_path
        self._set_icon_color = icon_color
        self._set_border_radius = radius

    # PAINT EVENT
    # painting the button and the icon
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # BRUSH
        brush = QBrush(QColor(self._set_bg_color))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width(), self.height())
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawRoundedRect(
            rect, 
            self._set_border_radius, 
            self._set_border_radius
        )

        # DRAW ICONS
        self.icon_paint(paint, self._set_icon_path, rect)

        # END PAINTER
        paint.end()

    # CHANGE STYLES
    # Functions with custom styles
    def change_style(self, event):
        if event == QEvent.Enter:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
            self.repaint()         
        elif event == QEvent.Leave:
            self._set_bg_color = self._bg_color
            self._set_icon_color = self._icon_color
            self.repaint()
        elif event == QEvent.MouseButtonPress:            
            self._set_bg_color = self._bg_color_pressed
            self._set_icon_color = self._icon_color_pressed
            self.repaint()
        elif event == QEvent.MouseButtonRelease:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
            self.repaint()

    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        #self.move_tooltip()
        #self.tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        #self.move_tooltip()
        #self.tooltip.hide()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            # SET FOCUS
            self.setFocus()
            # EMIT SIGNAL
            return self.clicked.emit()

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            # EMIT SIGNAL
            return self.released.emit()

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()
