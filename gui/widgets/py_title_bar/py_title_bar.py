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
        radius = 8
    ):
        super(PyTitleBar, self).__init__()

        settings = Settings()
        self.settings = settings.items

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
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            # if self.isMaximized():
            #     UiFunctions.maximize_restore(self)
            #     self.resize(_old_size)
            #     curso_x = self.pos().x()
            #     curso_y = event.globalPos().y() - QCursor.pos().y()
            #     self.move(curso_x, curso_y)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                parent.move(parent.pos() + event.globalPos() - parent.dragPos)
                parent.dragPos = event.globalPos()
                event.accept()
        self.top_logo.mouseMoveEvent = moveWindow
        self.title_label.mouseMoveEvent = moveWindow

        # ADD WIDGETS TO TITLE BAR
        self.bg_layout.addWidget(self.top_logo)
        self.bg_layout.addWidget(self.title_label)
        self.bg_layout.addWidget(self.right_frame)

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
        self.bg_layout.setContentsMargins(10,0,0,0)
        self.bg_layout.setSpacing(0)

        # LEFT FRAME WITH MOVE APP
        self.top_logo = QLabel()

        # TITLE LABEL
        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setStyleSheet("padding-left: 10px; font-size: 10pt")

        # RIGHT FRAME WITH BUTTONS
        self.right_frame = QFrame()
        self.right_frame.setMinimumWidth(100)
        self.right_frame.setStyleSheet("background: #CCC")

        # ADD TO LAYOUT
        self.title_bar_layout.addWidget(self.bg)