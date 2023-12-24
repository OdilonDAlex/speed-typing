# ------------------- #
# Interface principal #
# ------------------- #
import math
import time

from PySide6 import QtWidgets, QtCore, QtGui

from fakeTextGenerator import *


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speed Typing")

        self.game_run = False
        self.score = 0
        self.game_time = 60

        self.setWindowIcon(QtGui.QIcon("speedTyping.ico"))

        self.setup_ui()
        self.resize(1000, 400)
        self.time = None

        self.controller = None


    def setup_ui(self):
        self.create_widget()
        self.create_layout()
        self.add_widget_to_layout()
        self.setup_connection()
        self.modify_widget()
        self.game_loop()
        self.style_sheet()

    def create_widget(self):
        self.lbl_score = QtWidgets.QLabel('Score : --                   temps restant : --')
        self.lbl_fake_text = QtWidgets.QLabel('Fake text')
        self.indice = QtWidgets.QLabel('')
        self.ln_user_text = QtWidgets.QLineEdit()
        self.time = QtWidgets.QTimeEdit()

    def create_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.layout_for_lbl = QtWidgets.QHBoxLayout(self)

    def add_widget_to_layout(self):
        self.main_layout.addWidget(self.lbl_score)
        self.main_layout.addLayout(self.layout_for_lbl)
        self.main_layout.addWidget(self.indice)
        self.main_layout.addWidget(self.ln_user_text)

    def setup_connection(self):
        self.ln_user_text.textChanged.connect(self.check_text)

    def modify_widget(self):
        self.lbl_fake_text.setAlignment(QtGui.Qt.AlignCenter)
        self.ln_user_text.setFocus()
        self.ln_user_text.setAlignment(QtGui.Qt.AlignCenter)
        self.indice.setVisible(False)
        self.lbl_score.setAlignment(QtGui.Qt.AlignCenter)

    def game_loop(self):

        if not self.game_run:
            return
        if not self.time:
            self.time = time.time()

        for index in range(self.layout_for_lbl.count()):
            item = self.layout_for_lbl.itemAt(index)
            item.widget().deleteLater()

        text = get_game_text()

        lbl_list = [QtWidgets.QLabel(text[i]) for i in range(len(text))]

        for lbl in lbl_list:
            if not lbl.text():
                continue

            self.layout_for_lbl.addWidget(lbl)

    def check_text(self):

        self.time_out = False

        # game time verification
        if time.time() - self.time >= self.game_time:
            self.time_out = True

        # user text
        user_input = self.ln_user_text.text()

        true_response = 0

        for index in range(
                len(user_input) if len(user_input) <= self.layout_for_lbl.count() else self.layout_for_lbl.count()):
            item = self.layout_for_lbl.itemAt(index)
            item.widget().setStyleSheet(f"""
                QLabel {{
                        font-size : 30px ;
                        font-weight : 500 ; 
                        font-family : consolas;
                        color : {'green' if user_input[index] == item.widget().text() else 'red'} ;
                    }}
            """)
            if user_input[index] == item.widget().text():
                true_response += 1

            current_time = self.game_time - math.trunc(time.time() - self.time)

            self.lbl_score.setText(
                f"Score : {self.score}                  temps restant : {current_time if current_time >= 0 else 0} s")

            if self.time_out:
                self.message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, "Timeout", f"Score : {self.score}")

                self.message.setStyleSheet('width : 400px ; font-size : 20px ; ')

                self.message.exec()

                self.time = None
                self.game_loop()
                self.score = 0
                self.layout_for_lbl.setSpacing(0)
                self.ln_user_text.clear()

                self.controller.stop()

            if true_response == self.layout_for_lbl.count():
                if self.game_run:
                    self.game_loop()
                    self.style_sheet()

                    self.layout_for_lbl.setSpacing(0)

                    self.score += true_response

                    self.ln_user_text.clear()

    def style_sheet(self):

        self.lbl_score.setStyleSheet(f"""
            QLabel {{
                    font-size : 20px ;
                    font-weight : 400 ; 
                    font-family : 'courier' ;
                    color : rgb(220, 220, 250) ;
                }}
            """)

        self.lbl_score.setFixedHeight(20)

        for index in range(self.layout_for_lbl.count()):
            item = self.layout_for_lbl.itemAt(index)

            item.widget().setAlignment(QtGui.Qt.AlignCenter)
            item.widget().setStyleSheet(f"""
                    QLabel {{
                            font-size : 30px ;
                            font-weight : 600 ; 
                            color : rgb(200, 220, 230) ; 
                        }}
                """)

        self.ln_user_text.setFixedHeight(50)
        self.ln_user_text.setStyleSheet(f"""
            
        QLineEdit {{
                font-size : 30px ;
                border-radius : 5px ;  
                color : rgb(150, 150, 150) ; 
                border : 1px solid rgb(60, 60, 60 );
                background-color : rgb(50, 50, 50) ; 
            }}
                
        """)

        self.setStyleSheet("background-color : rgb(40, 40, 40) ; font-family : 'Gill Sans' ;")
        self.layout_for_lbl.setSpacing(0)

