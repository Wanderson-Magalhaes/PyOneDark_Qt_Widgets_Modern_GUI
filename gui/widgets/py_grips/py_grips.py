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

# PY GRIPS
# ///////////////////////////////////////////////////////////////
class PyGrips(QWidget):
    def __init__(self, parent, position, disable_color = False):

        # SETUP UI
        # ///////////////////////////////////////////////////////////////
        super().__init__()
        self.parent = parent
        self.setParent(parent)
        self.wi = Widgets()

        # SHOW TOP LEFT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "top_left":
            self.wi.top_left(self)
            grip = QSizeGrip(self.wi.top_left_grip)
            grip.setFixedSize(self.wi.top_left_grip.size())
            self.setGeometry(5, 5, 15, 15)
            
            # ENABLE COLOR
            if disable_color:
                self.wi.top_left_grip.setStyleSheet("background: transparent")

        # SHOW TOP RIGHT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "top_right":
            self.wi.top_right(self)
            grip = QSizeGrip(self.wi.top_right_grip)
            grip.setFixedSize(self.wi.top_right_grip.size())
            self.setGeometry(self.parent.width() - 20, 5, 15, 15)
            
            # ENABLE COLOR
            if disable_color:
                self.wi.top_right_grip.setStyleSheet("background: transparent")

        # SHOW BOTTOM LEFT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "bottom_left":
            self.wi.bottom_left(self)
            grip = QSizeGrip(self.wi.bottom_left_grip)
            grip.setFixedSize(self.wi.bottom_left_grip.size())
            self.setGeometry(5, self.parent.height() - 20, 15, 15)
            
            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_left_grip.setStyleSheet("background: transparent")

        # SHOW BOTTOM RIGHT GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "bottom_right":
            self.wi.bottom_right(self)
            grip = QSizeGrip(self.wi.bottom_right_grip)
            grip.setFixedSize(self.wi.bottom_right_grip.size())
            self.setGeometry(self.parent.width() - 20, self.parent.height() - 20, 15, 15)
            
            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_right_grip.setStyleSheet("background: transparent")

        # SHOW TOP GRIP
        # ///////////////////////////////////////////////////////////////
        if position == "top":
            self.wi.top(self)
            self.setGeometry(0, 5, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # RESIZE TOP
            def resize_top(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
                geo = self.parent.geometry()
                geo.setTop(geo.bottom() - height)
                self.parent.setGeometry(geo)
                event.accept()
            self.wi.top_grip.mouseMoveEvent = resize_top

            # ENABLE COLOR
            if disable_color:
                self.wi.top_grip.setStyleSheet("background: transparent")

        # SHOW BOTTOM GRIP
        # ///////////////////////////////////////////////////////////////
        elif position == "bottom":
            self.wi.bottom(self)
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # RESIZE BOTTOM
            def resize_bottom(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
                self.parent.resize(self.parent.width(), height)
                event.accept()
            self.wi.bottom_grip.mouseMoveEvent = resize_bottom

            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_grip.setStyleSheet("background: transparent")

        # SHOW LEFT GRIP
        # ///////////////////////////////////////////////////////////////
        elif position == "left":
            self.wi.left(self)
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # RESIZE LEFT
            def resize_left(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
                geo = self.parent.geometry()
                geo.setLeft(geo.right() - width)
                self.parent.setGeometry(geo)
                event.accept()
            self.wi.left_grip.mouseMoveEvent = resize_left

            # ENABLE COLOR
            if disable_color:
                self.wi.left_grip.setStyleSheet("background: transparent")

        # RESIZE RIGHT
        # ///////////////////////////////////////////////////////////////
        elif position == "right":
            self.wi.right(self)
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            def resize_right(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
                self.parent.resize(width, self.parent.height())
                event.accept()
            self.wi.right_grip.mouseMoveEvent = resize_right

            # ENABLE COLOR
            if disable_color:
                self.wi.right_grip.setStyleSheet("background: transparent")

    # MOUSE RELEASE
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        self.mousePos = None

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        if hasattr(self.wi, 'top_grip'):
            self.wi.top_grip.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'bottom_grip'):
            self.wi.bottom_grip.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'left_grip'):
            self.wi.left_grip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'right_grip'):
            self.wi.right_grip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'top_right_grip'):
            self.wi.top_right_grip.setGeometry(self.width() - 15, 0, 15, 15)

        elif hasattr(self.wi, 'bottom_left_grip'):
            self.wi.bottom_left_grip.setGeometry(0, self.height() - 15, 15, 15)

        elif hasattr(self.wi, 'bottom_right_grip'):
            self.wi.bottom_right_grip.setGeometry(self.width() - 15, self.height() - 15, 15, 15)


# GRIP WIDGTES
# ///////////////////////////////////////////////////////////////
class Widgets(object):
    def top_left(self, form):
        self.top_left_grip = QFrame(form)
        self.top_left_grip.setObjectName(u"top_left_grip")
        self.top_left_grip.setFixedSize(15, 15)
        self.top_left_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

    def top_right(self, form):
        self.top_right_grip = QFrame(form)
        self.top_right_grip.setObjectName(u"top_right_grip")
        self.top_right_grip.setFixedSize(15, 15)
        self.top_right_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

    def bottom_left(self, form):
        self.bottom_left_grip = QFrame(form)
        self.bottom_left_grip.setObjectName(u"bottom_left_grip")
        self.bottom_left_grip.setFixedSize(15, 15)
        self.bottom_left_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

    def bottom_right(self, form):
        self.bottom_right_grip = QFrame(form)
        self.bottom_right_grip.setObjectName(u"bottom_right_grip")
        self.bottom_right_grip.setFixedSize(15, 15)
        self.bottom_right_grip.setStyleSheet(u"background-color: #333; border: 2px solid #55FF00;")

    def top(self, form):
        self.top_grip = QFrame(form)
        self.top_grip.setObjectName(u"top_grip")
        self.top_grip.setGeometry(QRect(0, 0, 500, 10))
        self.top_grip.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.top_grip.setCursor(QCursor(Qt.SizeVerCursor))

    def bottom(self, form):
        self.bottom_grip = QFrame(form)
        self.bottom_grip.setObjectName(u"bottom_grip")
        self.bottom_grip.setGeometry(QRect(0, 0, 500, 10))
        self.bottom_grip.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.bottom_grip.setCursor(QCursor(Qt.SizeVerCursor))

    def left(self, form):
        self.left_grip = QFrame(form)
        self.left_grip.setObjectName(u"left")
        self.left_grip.setGeometry(QRect(0, 10, 10, 480))
        self.left_grip.setMinimumSize(QSize(10, 0))
        self.left_grip.setCursor(QCursor(Qt.SizeHorCursor))
        self.left_grip.setStyleSheet(u"background-color: rgb(255, 121, 198);")

    def right(self, form):
        self.right_grip = QFrame(form)
        self.right_grip.setObjectName(u"right")
        self.right_grip.setGeometry(QRect(0, 0, 10, 500))
        self.right_grip.setMinimumSize(QSize(10, 0))
        self.right_grip.setCursor(QCursor(Qt.SizeHorCursor))
        self.right_grip.setStyleSheet(u"background-color: rgb(255, 0, 127);")
