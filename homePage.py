# ------------------- #
# Home page interface #
# ------------------- #
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = None
        self.game_run = False
        self.setup_ui()

    def __str__(self):
        return "HOME_PAGE"

    def setup_ui(self):
        self.create_widget()
        self.create_layout()
        self.add_widget_to_layout()
        self.modify_widget()
        self.setup_connection()
        self.style_sheet()

    def create_widget(self):
        self.lbl_welcome = QLabel()
        self.lbl_welcome.setText("Bienvenue")
        self.btn_play = QPushButton("")
        self.btn_score = QPushButton("Score")
        self.btn_info = QPushButton("A propos")

    def create_layout(self):
        self.main_layout = QVBoxLayout()

        self.setLayout(self.main_layout)

    def add_widget_to_layout(self):
        self.main_layout.addWidget(self.lbl_welcome)
        self.main_layout.addWidget(self.btn_play)
        self.main_layout.addWidget(self.btn_score)
        self.main_layout.addWidget(self.btn_info)

    def modify_widget(self):
        list_btn = [self.btn_info, self.btn_score, self.btn_play]

        # button size policy and cursor
        for btn in list_btn:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # set spacing and button alignment to 'center'
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.setSpacing(10)

        # button size
        for btn in list_btn:
            if btn.text() == "":
                continue

            btn.setFixedSize(QSize(300, 40))

        self.btn_play.setFixedSize(QSize(300, 200))

        # button play icon
        self.btn_play.setFlat(True)
        self.btn_play.setIcon(QIcon("IMG-Play-background.png"))
        self.btn_play.setIconSize(QSize(300, 200))

        self.lbl_welcome.setAlignment(Qt.AlignCenter)

    def style_sheet(self):

        self.btn_info.setObjectName("main_btn")
        self.btn_score.setObjectName("main_btn")

        self.setStyleSheet(f"""
            * {{
                    background-color : rgb(40, 40, 40) ; 
                    color : rgb(40, 40, 40); 
                    font : 28px ;
                    font-weight : 700 ;
                    font-style : italic ; 
                }}
                
            #main_btn {{
                border-radius : 10px ;
                background-color : rgb(100, 100, 100) ;
            }}
            
            #main_btn::hover {{
                background-color : rgb(120, 120, 120) ; 
                }}
                
            QPushButton {{
                broder : none ;
                    }}
            QPushButton::hover {{
                    border : 1px solid rgb(190, 190, 220) ;
                    border-radius : 10px ;
                }}
                
            QLabel {{
                color : rgb(190, 190, 230) ;
                font-size : 40px ;
                font-style : italic ;  
                font-weight : 700 ;
            }}
                """)

    def setup_connection(self):
        self.btn_play.pressed.connect(self.play_game)

    def play_game(self):
        print("Play")
        self.game_run = True
        self.controller.play()


if __name__ == "__main__":
    app = QApplication()
    win = HomePage()
    win.show()
    app.exec()
