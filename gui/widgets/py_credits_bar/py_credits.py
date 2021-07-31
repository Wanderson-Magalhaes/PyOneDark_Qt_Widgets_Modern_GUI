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

# PY CREDITS BAR AND VERSION
# ///////////////////////////////////////////////////////////////
class PyCredits(QWidget):
    def __init__(
        self,
        copyright,
        version,
        bg_two,
        font_family,
        text_size,
        text_description_color,
        radius = 8,
        padding = 10
    ):
        super().__init__()

        # PROPERTIES
        self._copyright = copyright
        self._version = version
        self._bg_two = bg_two
        self._font_family = font_family
        self._text_size = text_size
        self._text_description_color = text_description_color
        self._radius = radius
        self._padding = padding

        # SETUP UI
        self.setup_ui()

    def setup_ui(self):
        # ADD LAYOUT
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0,0,0,0)

        # BG STYLE
        style = f"""
        #bg_frame {{
            border-radius: {self._radius}px;
            background-color: {self._bg_two};
        }}
        .QLabel {{
            font: {self._text_size}pt "{self._font_family}";
            color: {self._text_description_color};
            padding-left: {self._padding}px;
            padding-right: {self._padding}px;
        }}
        """

        # BG FRAME
        self.bg_frame = QFrame()
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(style)

        # ADD TO LAYOUT
        self.widget_layout.addWidget(self.bg_frame)

        # ADD BG LAYOUT
        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setContentsMargins(0,0,0,0)

        # ADD COPYRIGHT TEXT
        self.copyright_label = QLabel(self._copyright)
        self.copyright_label.setAlignment(Qt.AlignVCenter)

        # ADD VERSION TEXT
        self.version_label = QLabel(self._version)
        self.version_label.setAlignment(Qt.AlignVCenter)

        # SEPARATOR
        self.separator = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # ADD TO LAYOUT
        self.bg_layout.addWidget(self.copyright_label)
        self.bg_layout.addSpacerItem(self.separator)
        self.bg_layout.addWidget(self.version_label)
