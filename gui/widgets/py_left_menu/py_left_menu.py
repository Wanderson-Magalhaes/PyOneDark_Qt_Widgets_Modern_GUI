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

# IMPORT BUTTON AND DIV
# ///////////////////////////////////////////////////////////////
from . py_left_menu_button import PyLeftMenuButton
from . py_div import PyDiv

# PY LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyLeftMenu(QWidget):
    def __init__(
        self,
        parent = None,
        app_parent = None,
        dark_one = "#1b1e23",
        dark_three = "#21252d",
        dark_four = "#272c36",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        duration_time = 500,
        radius = 8,
        minimum_width = 50,
        maximum_width = 240,
        icon_path = "gui/images/svg_icons/icon_menu.svg",
        icon_path_close = "gui/images/svg_icons/icon_menu_close.svg",
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
        self._minimum_width = minimum_width
        self._maximum_width = maximum_width
        self._icon_path = icon_path
        self._icon_path_close = icon_path_close

        # SET PARENT
        self._parent = parent
        self._app_parent = app_parent

        # SETUP WIDGETS
        self.setup_ui()

        # SET BG COLOR
        self.bg.setStyleSheet(f"background: {dark_one}; border-radius: {radius};")

        self.button = PyLeftMenuButton(
            app_parent,
            "Add user menu", 
            "Test tooltip",
        )
        self.button.clicked.connect(lambda: self.toggle_animation())

        # TOGGLE BUTTON AND DIV MENUS
        # ///////////////////////////////////////////////////////////////
        self.toggle_button = PyLeftMenuButton(
            app_parent, 
            "Hide Menu", 
            "Expand/Retract menu",
            icon_path = icon_path
        )
        self.toggle_button.clicked.connect(self.toggle_animation)
        self.div_top = PyDiv(dark_four)

        # ADD TO TOP LAYOUT
        self.top_layout.addWidget(self.toggle_button)
        self.top_layout.addWidget(self.div_top)
        self.top_layout.addWidget(self.button) # Apagar

        # BUTTON WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.div_button = PyDiv(dark_four)
        self.settings_button = PyLeftMenuButton(
            app_parent, 
            "Settings", 
            "Open settings",
            icon_path="gui/images/svg_icons/icon_settings.svg"
        )
        self.bottom_layout.addWidget(self.div_button)
        self.bottom_layout.addWidget(self.settings_button)

    def toggle_animation(self):
        if self.toggle_button._is_toggle_active:
            self.toggle_button.set_active_toggle(False)
            self.toggle_button.set_icon(self._icon_path)
        else:
            self.toggle_button.set_active_toggle(True)
            self.toggle_button.set_icon(self._icon_path_close)

        self.animation = QPropertyAnimation(self._parent, b"minimumWidth")
        self.animation.stop()
        if self.width() == self._minimum_width:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._maximum_width)
            # ACTIVE
            self.button.set_active(True)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._minimum_width)
            # ACTIVE
            self.button.set_active(False)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._duration_time)      
        self.animation.start()        
        

    # SET APP LAYOUT
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self)
        self.left_menu_layout.setContentsMargins(0,0,0,0)

        # ADD BG
        self.bg = QFrame()

        # TOP FRAME
        self.top_frame = QFrame()

        # BOTTOM FRAME
        self.bottom_frame = QFrame()

        # ADD LAYOUTS
        self._layout = QVBoxLayout(self.bg)
        self._layout.setContentsMargins(0,0,0,0)

        # TOP LAYOUT
        self.top_layout = QVBoxLayout(self.top_frame)
        self.top_layout.setContentsMargins(0,0,0,0)
        self.top_layout.setSpacing(1)

        # BOTTOM LAYOUT
        self.bottom_layout = QVBoxLayout(self.bottom_frame)
        self.bottom_layout.setContentsMargins(0,0,0,0)
        self.bottom_layout.setSpacing(1)

        # ADD TOP AND BOTTOM FRAME
        self._layout.addWidget(self.top_frame, 0, Qt.AlignTop)
        self._layout.addWidget(self.bottom_frame, 0, Qt.AlignBottom)

        # ADD BG TO LAYOUT
        self.left_menu_layout.addWidget(self.bg)

        

        

