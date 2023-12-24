from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from homePage import HomePage
from app import MainWidget


class Controller(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('background-color : rgb(40, 40, 40) ;')

        self.home_page = HomePage()
        self.app_ = MainWidget()
        self.home_page.controller = self
        self.app_.controller = self
        self.setCentralWidget(self.home_page)

        self.setMinimumSize(QSize(1020, 500))

    def play(self):
        if self.home_page.game_run:
            self.app_.game_run = True
            self.app_.game_loop()
            self.app_.style_sheet()
            self.setCentralWidget(self.app_)
            self.app_.ln_user_text.setFocus()

    def stop(self):
        self.home_page.game_run = False
        self.app_.game_run = False
        self.home_page = HomePage()
        self.app_ = MainWidget()
        self.home_page.controller = self
        self.app_.controller = self
        self.setCentralWidget(self.home_page)

app = QApplication()
win = Controller()
win.show()
app.exec()