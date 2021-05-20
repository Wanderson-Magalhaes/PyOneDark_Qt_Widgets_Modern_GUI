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

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT DIV
# ///////////////////////////////////////////////////////////////
from . py_div import PyDiv

# IMPORT BUTTON
# ///////////////////////////////////////////////////////////////
from . py_title_button import PyTitleButton

# GLOBALS
# ///////////////////////////////////////////////////////////////
_is_maximized = False
_old_size = QSize()

# PY TITLE BAR
# Top bar with move application, maximize, restore, minimize,
# close buttons and extra buttons
# ///////////////////////////////////////////////////////////////
class PyTitleBar(QWidget):
    def __init__(
        self,
        parent,
        logo_image = "logo_top_100x22.svg",
        logo_width = 100,
        buttons = None,
        bg_color = "#343b48",
        div_color = "#3c4454",
        btn_bg_color = "#343b48",
        btn_bg_color_hover = "#3c4454",
        btn_bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#6c99f4",
        radius = 8,
        font_family = "Segoe UI",
        title_size = 10
    ):
        super(PyTitleBar, self).__init__()

        settings = Settings()
        self.settings = settings.items

        # PARAMETERS
        self._bg_color = bg_color
        self._div_color = div_color
        self._font_family = font_family
        self._title_size = title_size
        self._parent = parent
        self._btn_bg_color = btn_bg_color
        self._btn_bg_color_hover = btn_bg_color_hover
        self._btn_bg_color_pressed = btn_bg_color_pressed  
        self._context_color = context_color      
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active

        # SETUP UI
        self.setup_ui()

        # ADD BG COLOR
        self.bg.setStyleSheet(f"background-color: {bg_color}; border-radius: {radius}px;")

        # SET LOGO AND WIDTH
        self.top_logo.setMinimumWidth(logo_width)
        self.top_logo.setMaximumWidth(logo_width)
        self.top_logo.setPixmap(Functions.set_svg_image(logo_image))

        # ADD TITLE TEXT
        self.title_label.setText(self.settings["app_name"])

        # MOVE WINDOW / MAXIMIZE / RESTORE
        # ///////////////////////////////////////////////////////////////
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if parent.isMaximized():
                self.maximize_restore()
                #self.resize(_old_size)
                curso_x = parent.pos().x()
                curso_y = event.globalPos().y() - QCursor.pos().y()
                parent.move(curso_x, curso_y)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                parent.move(parent.pos() + event.globalPos() - parent.dragPos)
                parent.dragPos = event.globalPos()
                event.accept()

        # MOVE APP WIDGETS
        self.top_logo.mouseMoveEvent = moveWindow
        self.div_1.mouseMoveEvent = moveWindow
        self.title_label.mouseMoveEvent = moveWindow
        self.div_2.mouseMoveEvent = moveWindow

        # MAXIMIZE / RESTORE
        self.top_logo.mouseDoubleClickEvent = self.maximize_restore
        self.div_1.mouseDoubleClickEvent = self.maximize_restore
        self.title_label.mouseDoubleClickEvent = self.maximize_restore
        self.div_2.mouseDoubleClickEvent = self.maximize_restore

        # ADD WIDGETS TO TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.bg_layout.addWidget(self.top_logo)
        self.bg_layout.addWidget(self.div_1)
        self.bg_layout.addWidget(self.title_label)
        self.bg_layout.addWidget(self.div_2)

        # ADD BUTTONS BUTTONS
        # ///////////////////////////////////////////////////////////////
        # Functions
        self.minimize_button.clicked.connect(lambda: parent.showMinimized())
        self.maximize_restore_button.clicked.connect(lambda: self.maximize_restore())
        self.close_button.clicked.connect(lambda: parent.close())
        # ADD Buttons
        self.bg_layout.addWidget(self.minimize_button)
        self.bg_layout.addWidget(self.maximize_restore_button)
        self.bg_layout.addWidget(self.close_button)

    # MAXIMIZE / RESTORE
    # maximize and restore parent window
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self, e = None):
        global _is_maximized
        global _old_size
        
        # CHANGE UI AND RESIZE GRIP
        def change_ui():
            if _is_maximized:
                self._parent.ui.central_widget_layout.setContentsMargins(0,0,0,0)
                self._parent.ui.window.set_stylesheet(border_radius = 0, border_size = 0)
            else:
                self._parent.ui.central_widget_layout.setContentsMargins(10,10,10,10)
                self._parent.ui.window.set_stylesheet(border_radius = 10, border_size = 2)

        # CHECK EVENT
        if self._parent.isMaximized():
            _is_maximized = False
            self._parent.showNormal()
            change_ui()
        else:
            _is_maximized = True
            _old_size = QSize(self._parent.width(), self._parent.height())
            self._parent.showMaximized()
            change_ui()

    # SETUP APP
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.title_bar_layout = QVBoxLayout(self)
        self.title_bar_layout.setContentsMargins(0,0,0,0)

        # ADD BG
        self.bg = QFrame()

        # ADD BG LAYOUT
        self.bg_layout = QHBoxLayout(self.bg)
        self.bg_layout.setContentsMargins(10,0,5,0)
        self.bg_layout.setSpacing(0)

        # DIVS
        self.div_1 = PyDiv(self._div_color)
        self.div_2 = PyDiv(self._div_color)

        # LEFT FRAME WITH MOVE APP
        self.top_logo = QLabel()

        # TITLE LABEL
        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setStyleSheet(f'font: {self._title_size}pt "{self._font_family}"')

        # MINIMIZE BUTTON
        self.minimize_button = PyTitleButton(
            tooltip_text = "Close app",
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._btn_bg_color_pressed,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            icon_path = Functions.set_svg_icon("icon_minimize.svg")
        )

        # MAXIMIZE / RESTORE BUTTON
        self.maximize_restore_button = PyTitleButton(
            tooltip_text = "Maximize app",
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._btn_bg_color_pressed,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            icon_path = Functions.set_svg_icon("icon_maximize.svg")
        )

        # CLOSE BUTTON
        self.close_button = PyTitleButton(
            tooltip_text = "Close app",
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._context_color,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            icon_path = Functions.set_svg_icon("icon_close.svg")
        )

        # ADD TO LAYOUT
        self.title_bar_layout.addWidget(self.bg)