from PyQt6.QtGui import QPixmap, QImage
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

        self.static_scene = QGraphicsScene()
        pixmap_static = QPixmap("static.png")
        staticImage = QImage("static.png")
        pixmap_static.convertFromImage(staticImage)
        pixmap_static_item = self.static_scene.addPixmap(pixmap_static)
        pixmap_static_item.setPos(0,0)

        circle = QGraphicsEllipseItem(0, 0, 250, 250)
        self.static_scene.addItem(circle)

        self.news_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_news = QPixmap("news.png")
        pixmap_news_item = self.static_scene.addPixmap(pixmap_news)
        pixmap_news_item.setPos(0, 0)

        self.soap_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_soapOpera = QPixmap("soapOpera.png")
        pixmap_soapOpera_item = self.static_scene.addPixmap(pixmap_soapOpera)
        pixmap_soapOpera_item.setPos(0, 0)

        self.cartoon_scene = QGraphicsScene(0, 0, 250, 250)
        pixmap_cartoon = QPixmap("cartoon.png")
        pixmap_cartoon_item = self.static_scene.addPixmap(pixmap_cartoon)
        pixmap_cartoon_item.setPos(0, 0)

        self.graphicsView.setScene(self.soap_scene)
        self.graphicsView.show()


    def update(self):
        if self.__tenna.getStatus():
            self.ChSlider.setSliderPosition(int(self.__tenna.getChannel()))
        else:
            self.ChSlider.setSliderPosition(0)

        if self.__tenna.getStatus():
            if self.__tenna.getChannel() == 0:
                self.graphicsView.setScene(self.static_scene)
            if self.__tenna.getChannel() == 1:
                self.graphicsView.setScene(self.soap_scene)
            if self.__tenna.getChannel() == 2:
                self.graphicsView.setScene(self.cartoon_scene)
            if self.__tenna.getChannel() == 3:
                self.graphicsView.setScene(self.news_scene)



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




