#coding: utf8

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from win10toast import ToastNotifier

class KunmingWeather:
    def __init__(self):
        page = requests.get("http://www.weather.com.cn/weather/101290101.shtml")
        self.soup = BeautifulSoup(page.content, 'html.parser')
    
    def get_latest_7_days(self):
        weather_kunming_7days = []
        for day in range(7):
            weather_kunming_7days.append({
                "date": self.soup.select("li.sky.skyid")[0].find_all('h1')[0].text,
                "weather": self.soup.select("li.sky.skyid")[0].select('p.wea')[0].text.strip(),
                "temperature": self.soup.select("li.sky.skyid")[0].select('p.tem')[0].text
            })
        return weather_kunming_7days
    
    def get_around(self):
        weather_kunming_around = []
        for index in range(len(self.soup.select("div.aro_city ul li"))):
            liTag = self.soup.select("div.aro_city ul li")[index]
            weather_kunming_around.append({
                "name": liTag.select("span")[0].text,
                "temperature": liTag.select("i")[0].text
            })
        return weather_kunming_around

if __name__ == "__main__":
    kunmingWeather = KunmingWeather()
    weather_latest_7_days = kunmingWeather.get_latest_7_days()
    weather_around = kunmingWeather.get_around()
    pprint(weather_latest_7_days)
    pprint(weather_around)
    # 汇总7天的天气情况
    weather_latest_7_days_content = ", ".join(map(lambda weather_info: "日期：{date}, 天气：{weather}, 温度：{temperature}".format(**weather_info), weather_latest_7_days))
    # 汇总周边天气的情况
    weather_around_content = ", ".join(map(lambda weather_info: "地点：{name}, 温度：{temperature}".format(**weather_info), weather_around))
    toaster = ToastNotifier()
    # 汇总整体Toast信息
    weather_contents = '''
    昆明最近七天的天气如下：
    {weather_latest_7_days_content}
    昆明周边的天气如下：
    {weather_around_content}
    '''.format(weather_latest_7_days_content=weather_latest_7_days_content,weather_around_content=weather_around_content)
    # 显示Toast弹窗
    toaster.show_toast("Kunming Weather Notification", weather_contents)