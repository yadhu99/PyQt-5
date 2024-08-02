import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QGridLayout,
    QFrame,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtGui import QPalette, QLinearGradient, QColor, QIcon
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title of the main window
        self.setWindowTitle("Garmin2400")
        self.setGeometry(100, 100, 800, 600)

        self.set_background_gradient()

        self.home_page = None
        self.subpages = {}

        # Create and set up the header
        self.header_widget = QWidget(self)
        self.header_widget.setGeometry(0, 0, 800, 50)
        self.header_widget.setStyleSheet("background-color: #12202D;")
        header_layout = QHBoxLayout(self.header_widget)
        header_layout.setContentsMargins(10, 10, 10, 10)
        header_layout.setSpacing(10)

        for _ in range(4):
            header_layout.addWidget(QWidget(self.header_widget))

        self.header_widget.setLayout(header_layout)

        self.separator_line = QFrame(self)
        self.separator_line.setGeometry(0, 50, 800, 1)
        self.separator_line.setStyleSheet("background-color: white;")

        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(350, 60, 100, 50)
        self.home_button.clicked.connect(self.show_home_page)

        self.footer_widget = QWidget(self)
        self.footer_widget.setGeometry(0, 530, 810, 80)
        self.footer_widget.setStyleSheet(
            """
            background: qlineargradient(
                spread:pad, x1:0, y1:0, x2:0, y2:1,
                stop:0 #88B9E5,  
                stop:1 #376FA1    
            );
            """
        )

        footer_layout = QHBoxLayout(self.footer_widget)
        footer_layout.setContentsMargins(10, 10, 10, 10)
        footer_layout.setSpacing(10)

        back_icon_path = "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/back.png"
        msg_icon_path = "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/letter-m.png"
        demo_icon_path = "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/letter-d.png"

        # Create footer buttons and add them to the layout
        button_size = 60

        self.back_footer_button = QPushButton("Back", self.footer_widget)
        self.back_footer_button.setFixedSize(button_size, button_size)
        self.back_footer_button.setIcon(QIcon(back_icon_path))
        self.back_footer_button.setIconSize(QSize(30, 30))
        self.back_footer_button.setStyleSheet(
            """
            QPushButton {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1E5587, 
                    stop:1 #010203   
                );
                color: white;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                border: 2px solid #FFFFFF; 
            }
            """
        )
        self.back_footer_button.clicked.connect(self.show_main_window)

        self.msg_footer_button = QPushButton("Msg", self.footer_widget)
        self.msg_footer_button.setFixedSize(button_size, button_size)
        self.msg_footer_button.setIcon(QIcon(msg_icon_path))
        self.msg_footer_button.setIconSize(QSize(30, 30))
        self.msg_footer_button.setStyleSheet(
            """
            QPushButton {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1E5587, 
                    stop:1 #010203  
                );
                color: white;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                border: 2px solid #FFFFFF; 
            }
            """
        )
        self.msg_footer_button.clicked.connect(
            lambda: self.show_msg_page("Message from Footer")
        )

        self.demo_footer_button = QPushButton("Demo", self.footer_widget)
        self.demo_footer_button.setFixedSize(button_size, button_size)
        self.demo_footer_button.setIcon(QIcon(demo_icon_path))
        self.demo_footer_button.setIconSize(QSize(30, 30))
        self.demo_footer_button.setStyleSheet(
            """
            QPushButton {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1E5587,  
                    stop:1 #010203   
                );
                color: white;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                border: 2px solid #FFFFFF;
            }
            """
        )
        self.demo_footer_button.clicked.connect(self.show_demo_page)

        footer_layout.addWidget(self.back_footer_button)
        footer_layout.addSpacerItem(
            QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        )  # Spacer between buttons
        footer_layout.addWidget(self.msg_footer_button)
        footer_layout.addSpacerItem(
            QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        )  # Spacer between buttons
        footer_layout.addWidget(self.demo_footer_button)

        footer_layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self.footer_widget.setLayout(footer_layout)

    def set_background_gradient(self):
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#0A151E"))  # Dark blue
        gradient.setColorAt(1.0, QColor("#3477B3"))  # Light blue
        palette = QPalette()
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

    def show_home_page(self):
        self.home_button.hide()

        if self.home_page is None:
            self.home_page = QWidget(self)
            layout = QGridLayout(self.home_page)
            layout.setHorizontalSpacing(1)
            layout.setVerticalSpacing(10)
            layout.setContentsMargins(10, 0, 3, 18)

            subpage_icons = {
                "Map": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/planet-earth (2).png",
                "Traffic": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/management (1).png",
                "Terrain": "/Users/yadhu/Downloads/snowed-mountains.png",
                "Weather": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/storm (1).png",
                "FlightPlan": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/flight-route.png",
                "Proc": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/maintenance.png",
                "Charts": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/charts.png",
                "Nearest": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/airplane.png",
                "Waypoint Info": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/way.png",
                "Services": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/customer-service.png",
                "Utilities": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/tool.png",
                "System": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/repair.png",
                "Emergency": "/Users/yadhu/PROJECTS/pyqt copy/pictures pyqt/emergency.png",
            }

            for index, (subpage, icon_path) in enumerate(subpage_icons.items()):
                button = QPushButton(self.home_page)
                button.setFixedSize(90, 90)
                button.setIcon(QIcon(icon_path))
                button.setIconSize(QSize(0, 60))
                button.setStyleSheet(
                    """
                    QPushButton {
                        background: qlineargradient(
                            spread:pad, x1:0, y1:0, x2:0, y2:1,
                            stop:0 #1E5587, 
                            stop:1 #010203  
                        );
                        color: white;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton::icon {
                        alignment: top; 
                    }
                    QPushButton:hover {
                        border: 2px solid #FFFFFF; 
                    }
                    """
                )

                button_layout = QVBoxLayout(button)
                button_layout.setContentsMargins(0, 0, 0, 0)
                button_layout.setSpacing(0)

                icon_label = QLabel(button)
                icon_label.setPixmap(QIcon(icon_path).pixmap(60, 60))
                icon_label.setAlignment(Qt.AlignCenter)
                button_layout.addWidget(icon_label)

                text_label = QLabel(subpage, button)
                text_label.setStyleSheet("color: white;")
                text_label.setAlignment(Qt.AlignCenter)
                button_layout.addWidget(text_label)

                button.clicked.connect(
                    lambda _, sp=subpage: self.show_subpage(sp)
                )
                row = index // 4
                col = index % 4
                layout.addWidget(button, row, col, Qt.AlignCenter)

            self.home_page.setLayout(layout)
            self.home_page.setGeometry(50, 100, 600, 400)

        self.home_page.show()

        if self.subpages:
            for subpage in self.subpages.values():
                subpage.hide()

    def show_subpage(self, subpage_name):
        self.home_page.hide()

        if subpage_name not in self.subpages:
            subpage_widget = QWidget(self)
            layout = QVBoxLayout(subpage_widget)

            subpage_widget.setStyleSheet(
                """
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #010909,  
                    stop:1 #36A0CA  
                );
                """
            )

            label = QLabel(subpage_name, subpage_widget)
            label.setStyleSheet("color: white;")
            layout.addWidget(label)

            back_button = QPushButton("Back", subpage_widget)
            back_button.clicked.connect(self.show_home_page)
            layout.addWidget(back_button)

            subpage_widget.setLayout(layout)
            subpage_widget.setGeometry(150, 100, 400, 300)

            self.subpages[subpage_name] = subpage_widget

        self.subpages[subpage_name].show()

    def show_main_window(self):
        # Hide home page and subpages, and show main window
        if self.home_page:
            self.home_page.hide()

        if self.subpages:
            for subpage in self.subpages.values():
                subpage.hide()

        self.home_button.show()
        self.show()

    def show_msg_page(self, message):
        self.home_page.hide()

        if "MsgPage" not in self.subpages:
            self.subpages["MsgPage"] = QWidget(self)
            layout = QVBoxLayout(self.subpages["MsgPage"])

            self.subpages["MsgPage"].setStyleSheet(
                """
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #ADD8E6,  
                    stop:1 #000000  
                );
                """
            )

            label = QLabel(message, self.subpages["MsgPage"])
            label.setStyleSheet("color: white;")
            layout.addWidget(label)

            back_button = QPushButton("Back", self.subpages["MsgPage"])
            back_button.clicked.connect(self.show_main_window)
            layout.addWidget(back_button)

            self.subpages["MsgPage"].setLayout(layout)
            self.subpages["MsgPage"].setGeometry(150, 100, 400, 300)

        self.subpages["MsgPage"].show()

    def show_demo_page(self):
        self.home_page.hide()

        if "DemoPage" not in self.subpages:
            self.subpages["DemoPage"] = QWidget(self)
            layout = QVBoxLayout(self.subpages["DemoPage"])

            self.subpages["DemoPage"].setStyleSheet(
                """
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #010909,  
                    stop:1 #000000 
                );
                """
            )

            demo_label = QLabel("Demo Content", self.subpages["DemoPage"])
            demo_label.setStyleSheet("color: white;")
            layout.addWidget(demo_label)

            back_button = QPushButton("Back", self.subpages["DemoPage"])
            back_button.clicked.connect(self.show_main_window)
            layout.addWidget(back_button)

            self.subpages["DemoPage"].setLayout(layout)
            self.subpages["DemoPage"].setGeometry(150, 100, 400, 300)

        self.subpages["DemoPage"].show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
