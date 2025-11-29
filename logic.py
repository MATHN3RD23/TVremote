from PyQt6.QtWidgets import *
from gui import *
from television import *

class CoolTelevision(Television):
    def __init__(self):
        super().__init__()
        self.__settings = False
        self.__channelList = False

    def channel_up(self) -> None:
        super().channel_down()
        if self.__channelList:
            self.__channelList = False

    def channel_down(self) -> None:
        super().channel_down()
        if self.__channelList:
            self.__channelList = False

    def power(self) -> None:
        super().power()
        if self.__channelList:
            self.__channelList = False
        if self.__settings:
            self.__settings = False

    def settings(self) -> None:
        if not self.__settings:
            self.__settings = True

    def channel_list(self) -> None:
        if not self.__channelList:
            self.__channelList = True


    def exit(self) -> None:
        if self.__channelList or self.__settings:
            self.__channelList = False
            self.__settings = False

#separating TV logic and Gui logic


class Logic(QMainWindow, Ui_TVremoteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        tenna = Television()

    def update(self):
        #updates the visual gui
        pass

