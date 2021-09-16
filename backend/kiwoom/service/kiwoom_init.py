from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *


class InitWindow(QMainWindow):
    ocx = None

    def __init__(self):
        super().__init__()
        if InitWindow.ocx is None:
            InitWindow.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
            print("login")





