from PyQt6.QtGui import QPixmap, QBrush, QFont
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from gui import *
from coolTV import *


"""
NOTE: the images used are implemented with absolute path and may need re-worked with implementing
lines of occurance:
42, 46, 51, 56, 61, 66, 71, 94
"""


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
        self.powerButton.clicked.connect(self.clicked_power)
        self.oneButton.clicked.connect(self.clicked_1)
        self.twoButton.clicked.connect(self.clicked_2)
        self.threeButton.clicked.connect(self.clicked_3)
        self.fourButton.clicked.connect(self.clicked_4)
        self.fiveButton.clicked.connect(self.clicked_5)
        self.sixButton.clicked.connect(self.clicked_6)
        self.sevenButton.clicked.connect(self.clicked_7)
        self.eightButton.clicked.connect(self.clicked_8)
        self.nineButton.clicked.connect(self.clicked_9)
        self.settingsButton.clicked.connect(self.click_settings)
        self.ChListButton.clicked.connect(self.click_chList)
        self.ExitButton.clicked.connect(self.click_back)
        self.ChSlider.valueChanged.connect(self.slider_change)

        self.static_scene = QGraphicsScene(0,0,250,250)
        pixmap_static = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/static.png")
        pixmap_static_item = self.static_scene.addPixmap(pixmap_static)

        self.news_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_news = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/news.png")
        pixmap_news_item = self.news_scene.addPixmap(pixmap_news)
        pixmap_news_item.setPos(0, 0)

        self.soap_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_soapOpera = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/soapOpera.png")
        pixmap_soapOpera_item = self.soap_scene.addPixmap(pixmap_soapOpera)
        pixmap_soapOpera_item.setPos(0, 0)

        self.cartoon_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_cartoon = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/cartoon.png")
        pixmap_cartoon_item = self.cartoon_scene.addPixmap(pixmap_cartoon)
        pixmap_cartoon_item.setPos(0, 0)

        self.ad_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_ad = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/ad.png")
        pixmap_ad_item = self.ad_scene.addPixmap(pixmap_ad)
        pixmap_ad_item.setPos(0, 0)

        self.chList_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_chL = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/chList.png")
        pixmap_chL_item = self.chList_scene.addPixmap(pixmap_chL)
        pixmap_chL_item.setPos(0, 0)

        self.setting_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_setting = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/setting.png")
        pixmap_setting_item = self.setting_scene.addPixmap(pixmap_setting)
        pixmap_setting_item.setPos(0, 0)

        self.volume_bar = QGraphicsRectItem(0, 0, int(self.__tenna.getVolume() * 10), 10)
        brush = QBrush(Qt.GlobalColor.black)
        self.volume_bar.setBrush(brush)
        self.setting_scene.addItem(self.volume_bar)

        self.ch_text = QGraphicsTextItem("")
        self.setting_scene.addItem(self.ch_text)


        self.empty_scene = QGraphicsScene(0, 0, 250, 250)


        self.graphicsView.setScene(self.empty_scene)
        self.graphicsView.show()


    def settings_scene_setup(self):
        self.setting_scene.clear()

        pixmap_setting = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/TVremote/setting.png")
        pixmap_setting_item = self.setting_scene.addPixmap(pixmap_setting)
        pixmap_setting_item.setPos(0, 0)

        if self.__tenna.getMuted():
            self.volume_bar = QGraphicsRectItem(30, 80, int(0 * 50), 30)
            brush = QBrush(Qt.GlobalColor.black)
            self.volume_bar.setBrush(brush)
            self.setting_scene.addItem(self.volume_bar)
        else:
            self.volume_bar = QGraphicsRectItem(30, 80, int(self.__tenna.getVolume() * 50) + 50, 30)
            brush = QBrush(Qt.GlobalColor.black)
            self.volume_bar.setBrush(brush)
            self.setting_scene.addItem(self.volume_bar)

        self.ch_text = QGraphicsTextItem(str(self.__tenna.getChannel()))
        self.ch_text.setPos(30, 180)
        self.ch_text.setDefaultTextColor(Qt.GlobalColor.black)
        self.ch_text.setFont(QFont("Helvetica", 25, 1, False))
        self.setting_scene.addItem(self.ch_text)


    def update(self):
        if self.__tenna.getStatus():
            self.ChSlider.setSliderPosition(int(self.__tenna.getChannel()))
        else:
            self.ChSlider.setSliderPosition(0)

        if self.__tenna.getStatus():
            if not self.__tenna.getChannelList() and not self.__tenna.getSettings():
                if self.__tenna.getChannel() == 3:
                    self.graphicsView.setScene(self.ad_scene)
                elif self.__tenna.getChannel() == 2:
                    self.graphicsView.setScene(self.soap_scene)
                elif self.__tenna.getChannel() == 1:
                    self.graphicsView.setScene(self.cartoon_scene)
                elif self.__tenna.getChannel() == 0:
                    self.graphicsView.setScene(self.news_scene)
                else:
                    self.graphicsView.setScene(self.static_scene)

            elif self.__tenna.getChannelList():
                self.graphicsView.setScene(self.chList_scene)
            elif self.__tenna.getSettings():
                self.settings_scene_setup()
                self.graphicsView.setScene(self.setting_scene)
        else:
            self.graphicsView.setScene(self.empty_scene)


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

    def clicked_power(self):
        self.__tenna.power()
        self.update()

    def clicked_0(self):
        self.__tenna.setChannel(0)
        self.update()
    def clicked_1(self):
        self.__tenna.setChannel(1)
        self.update()
    def clicked_2(self):
        self.__tenna.setChannel(2)
        self.update()
    def clicked_3(self):
        self.__tenna.setChannel(3)
        self.update()
    def clicked_4(self):
        self.__tenna.setChannel(4)
        self.update()
    def clicked_5(self):
        self.__tenna.setChannel(5)
        self.update()
    def clicked_6(self):
        self.__tenna.setChannel(6)
        self.update()
    def clicked_7(self):
        self.__tenna.setChannel(7)
        self.update()
    def clicked_8(self):
        self.__tenna.setChannel(8)
        self.update()
    def clicked_9(self):
        self.__tenna.setChannel(9)
        self.update()

    def click_chList(self):
        self.__tenna.channel_list()
        self.update()

    def click_settings(self):
        self.__tenna.settings()
        self.update()

    def click_back(self):
        self.__tenna.exit()
        self.update()

    def slider_change(self):
        self.__tenna.setChannel(self.ChSlider.sliderPosition())
        self.update()




