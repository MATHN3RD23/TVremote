from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_TVremoteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
