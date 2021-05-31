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

# IMPORT CLOSE BUTTON
# ///////////////////////////////////////////////////////////////
from . py_left_button import *

# IMPORT LEFT COLUMN
# ///////////////////////////////////////////////////////////////
from gui.uis.columns.ui_left_column import Ui_LeftColumn

class PyLeftColumn(QWidget):
    def __init__(
        self,
        parent,
        app_parent,
        text_title,
        text_title_size,
        text_title_color,
        dark_one,
        bg_color,
        btn_color,
        btn_color_hover,
        btn_color_pressed,
        icon_path,
        icon_color,
        icon_color_hover,
        icon_color_pressed,
        icon_close_path,
        radius = 8
    ):
        super().__init__()

        # PARAMETERS
        self._parent = parent
        self._app_parent = app_parent
        self._text_title = text_title
        self._text_title_size = text_title_size
        self._text_title_color = text_title_color
        self._icon_path = icon_path
        self._dark_one = dark_one
        self._bg_color = bg_color
        self._btn_color = btn_color
        self._btn_color_hover = btn_color_hover
        self._btn_color_pressed = btn_color_pressed
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_close_path = icon_close_path
        self._radius = radius

        # SETUP UI
        self.setup_ui()

        # ADD LEFT COLUMN TO BG FRAME
        self.left_column = Ui_LeftColumn()
        self.left_column.setupUi(self.content_frame)

    def setup_ui(self):
        # BASE LAYOUT
        self.base_layout = QVBoxLayout(self)
        self.base_layout.setContentsMargins(0,0,0,0)
        self.base_layout.setSpacing(0)

        # TITLE FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_frame = QFrame()
        self.title_frame.setMaximumHeight(47)
        self.title_frame.setMinimumHeight(47)

        # TITLE BASE LAYOUT 
        self.title_base_layout = QVBoxLayout(self.title_frame)
        self.title_base_layout.setContentsMargins(5,3,5,3)

        # TITLE BG
        self.title_bg_frame = QFrame()
        self.title_bg_frame.setObjectName("title_bg_frame")
        self.title_bg_frame.setStyleSheet(f'''
        #title_bg_frame {{
            background-color: {self._bg_color};
            border-radius: {self._radius}px;
        }}
        ''')

        # LAYOUT TITLE BG
        self.title_bg_layout = QHBoxLayout(self.title_bg_frame)
        self.title_bg_layout.setContentsMargins(5,5,5,5)

        # ICON
        self.icon_frame = QFrame()
        self.icon_frame.setFixedSize(30,30)
        self.icon_frame.setStyleSheet("background: none;")
        self.icon_layout = QVBoxLayout(self.icon_frame)
        self.icon_layout.setContentsMargins(0,0,0,0)
        self.icon_layout.setSpacing(5)
        self.icon = QSvgWidget(self._icon_path)
        self.icon_layout.addWidget(self.icon, Qt.AlignCenter, Qt.AlignCenter)

        # LABEL
        self.title_label = QLabel(self._text_title)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(f'''
        #title_label {{
            font-size: {self._text_title_size}pt;
            color: {self._text_title_color};
            padding-bottom: 2px;
            background: none;
        }}
        ''')

        # BTN FRAME
        self.btn_frame = QFrame()
        self.btn_frame.setFixedSize(30,30)
        self.btn_frame.setStyleSheet("background: none;")
        # CLOSE BUTTON
        self.btn_close = PyLeftButton(
            self._parent,
            self._app_parent,
            tooltip_text = "Hide",
            dark_one = self._dark_one,
            bg_color = self._btn_color,
            bg_color_hover = self._btn_color_hover,
            bg_color_pressed = self._btn_color_pressed,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_pressed,
            context_color = self._icon_color_pressed,
            text_foreground = self._text_title_color,
            icon_path = self._icon_close_path,
            radius = 6,
        )
        self.btn_close.setParent(self.btn_frame)


        # ADD TO TITLE LAYOUT
        self.title_bg_layout.addWidget(self.icon_frame)
        self.title_bg_layout.addWidget(self.title_label)
        self.title_bg_layout.addWidget(self.btn_frame)

        # ADD TITLE BG TO LAYOUT
        self.title_base_layout.addWidget(self.title_bg_frame)

        # CONTENT FRAME
        # ///////////////////////////////////////////////////////////////
        self.content_frame = QFrame()
        self.content_frame.setStyleSheet("background: none")

        # ADD TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.base_layout.addWidget(self.title_frame)
        self.base_layout.addWidget(self.content_frame)
