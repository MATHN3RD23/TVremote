from PyQt6.QtWidgets import *
from gui import *
from coolTV import *



class Logic(QMainWindow, Ui_TVremoteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        tenna = CoolTelevision()

    def update(self):
        #updates the visual gui
        pass

