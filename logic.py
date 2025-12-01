from PyQt6.QtWidgets import *
from gui import *
from coolTV import *



class Logic(QMainWindow, Ui_TVremoteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__tenna = CoolTelevision()
        self.muteButton.clicked.connect(self.clicked_mute)
        self.CHupButton.clicked.connect(self.clicked_CHup)
        self.CHdownButton.clicked.connect(self.clicked_CHdown)
        self.VOLupButton.clicked.connect(self.clicked_volUp)
        self.VOLdownButton.clicked.connect(self.clicked_volDown)


    def update(self):
        self.ChSlider.setSliderPosition(int(self.__tenna.getChannel()))
        return

    def clicked_mute(self):
        self.__tenna.mute()
        self.update()
        return

    def clicked_CHup(self):
        self.__tenna.channel_up()
        self.update()

    def clicked_CHdown(self):
        self.__tenna.channel_down()
        self.update()

    def clicked_volDown(self):
        self.__tenna.volume_down()
        self.update()

    def clicked_volUp(self):
        self.__tenna.volume_up()
        self.update()



