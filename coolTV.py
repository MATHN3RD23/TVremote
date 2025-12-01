from television import *

class CoolTelevision(Television):
    def __init__(self):
        super().__init__()
        self.__settings = False
        self.__channelList = False

    def channel_up(self) -> None:
        super().channel_up()
        self.__channelList = False

    def channel_down(self) -> None:
        super().channel_down()
        if self.getChannel() > self.MAX_CHANNEL:
            self.setChannel(self.MAX_CHANNEL)
        self.__channelList = False

    def power(self) -> None:
        super().power()
        self.__channelList = False
        self.__settings = False

    def settings(self) -> None:
        if not self.__settings:
            self.__settings = True

    def channel_list(self) -> None:
        if not self.__channelList:
            self.__channelList = True


    def exit(self) -> None:
        self.__channelList = False
        self.__settings = False