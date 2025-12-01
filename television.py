"""
Imported from Lab 12
"""

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method initializes the television
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    #added code-----
    def getChannel(self) -> int:
        return self.__channel

    def getStatus(self):
        return self.__status

    def setChannel(self, channel: int) -> None:
        self.__channel = channel
    #end added code----

    def power(self)-> None:
        """
        Method switches the current power status
        """
        self.__status = not self.__status

    def mute(self)-> None:
        """
        Method switches the current muted status
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self)-> None:
        """
        Method raises the current channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self)-> None:
        """
        Method lowers the current channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
               self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self)-> None:
        """
        Method raises the current volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self)-> None:
        """
        Method lowers the current volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method prints out the current status of the television
        :return: tv status
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
