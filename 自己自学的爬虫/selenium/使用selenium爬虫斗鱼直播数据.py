import time
import plotly as py
import plotly.graph_objs as go
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re


class DouYuSpider(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/g_CF'
        self.data = {'大于100万': 0, '大于80万': 0, '大于60万': 0, '大于40万': 0, '大于20万': 0, '大于10万': 0, '小于10万': 0}
        self.firefoxBinery = FirefoxBinary(firefox_path='/home/mrxu/Downloads/firefox/firefox-bin')
        self.page = 1

    def get_response(self):
        river = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckord0.26/geckodriver',
                                  firefox_binary=self.firefoxBinery)
        river.get(self.url)
        while True:
            time.sleep(3)
            hot_num = river.find_elements_by_class_name('DyListCover-hot')
            info = river.find_elements_by_class_name('DyListCover-intro')
            river.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

            for num in zip(hot_num, info):
                # print('这个是数据',num[0].text)
                if '万' in num[0].text:
                    num = float(str(num[0].text).replace('万', '')) * 10000
                else:
                    num = float(num[0].text)
                if num >= 1000000:
                    self.data['大于100万'] += 1
                elif num >= 800000:
                    self.data['大于80万'] += 1
                elif num >= 600000:
                    self.data['大于60万'] += 1
                elif num >= 400000:
                    self.data['大于40万'] += 1
                elif num >= 200000:
                    self.data['大于20万'] += 1
                elif num >= 100000:
                    self.data['大于10万'] += 1
                elif num <= 100000:
                    self.data['小于10万'] += 1

            next = river.find_element_by_class_name('dy-Pagination-next')
            is_next = str(next.get_attribute('aria-disabled')).capitalize()

            if is_next == 'False':
                next.click()
            else:
                river.quit()
                break

        self.create_bar()

    def create_bar(self):
        pyplt = py.offline.plot
        # Traces
        trace_1 = go.Bar(
            x=list(self.data.keys()),
            y=list(self.data.values()),
            name="201609"
        )

        trace = [trace_1]
        # Layout
        layout = go.Layout(
            title='斗鱼数据分析'
        )
        # Figure
        figure = go.Figure(data=trace, layout=layout)
        # Plot
        pyplt(figure, filename='斗鱼数据分析.html')


if __name__ == '__main__':
    dys = DouYuSpider()
    dys.get_response()
