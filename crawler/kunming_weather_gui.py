#coding: utf-8

from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QApplication, QMainWindow, QActionGroup, QAction
import sys
import os
# import qdarkstyle
# import qdarkgraystyle
from kunming_weather import KunmingWeather
# import PyQt5_stylesheets
app = None

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('simple_weather.ui', self)
        kunmingWeather = KunmingWeather()
        weather_latest_7_days = kunmingWeather.get_latest_7_days()
        weather_around = kunmingWeather.get_around()
        # 汇总7天的天气情况
        self.weather_latest_7_days_content = "\n".join(map(lambda weather_info: "日期：{date}, 天气：{weather}, 温度：{temperature}".format(**weather_info), weather_latest_7_days))
        # 汇总周边天气的情况
        self.weather_around_content = "\n".join(map(lambda weather_info: "地点：{name}, 温度：{temperature}".format(**weather_info), weather_around))

        self.show()

    @pyqtSlot()
    def on_button_clicked(self):
        button = self.sender()
        text = button.text()
        if text == "最近七天天气":
            self.textEditResult.setText(self.weather_latest_7_days_content)
        elif text == "周边天气情况":
            self.textEditResult.setText(self.weather_around_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())