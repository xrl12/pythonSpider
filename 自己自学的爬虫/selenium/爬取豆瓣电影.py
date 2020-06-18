from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import re


class DouBanSpider(object):
    def __init__(self):
        self.firefoxBinery = FirefoxBinary(firefox_path='/home/mrxu/Downloads/firefox/firefox-bin')
        self.driver = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckord0.26/geckodriver',
                                        firefox_binary=self.firefoxBinery)

    def send_request(self, url, kw='李连杰'):
        print('正在发送的路由是{}'.format(url))
        self.driver.get(url)
        sleep(2)
        input = self.get_input()
        btn = self.get_btn()
        input.send_keys(kw)
        btn.click()
        while True:
            print('正在获取页面元素')
            div_list = self.driver.find_elements_by_class_name('item-root')
            sleep(3)
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            for div in div_list[1:]:
                title = div.find_element_by_class_name('title').text
                abstract = div.find_element_by_xpath(".//div[@class='meta abstract']").text
                rating_pl = div.find_element_by_xpath(".//div[@class='rating sc-bwzfXH hxNRHc']")
                yanyuan = div.find_element_by_xpath(".//div[@class='meta abstract_2']").text
                try:
                    rating = rating_pl.find_element_by_class_name('rating_nums').text
                except:
                    rating = 0

                try:
                    pl = rating_pl.find_element_by_class_name('pl').text
                    pl_nums = re.search('\d+',pl).group()
                except:
                    pl_nums = 0
                print(title)
            try:
                next = self.driver.find_element_by_class_name('next')
                next.click()
            except:
                self.driver.quit()
                break

    def get_input(self):
        return self.driver.find_element_by_id('inp-query')

    def get_btn(self):
        return self.driver.find_element_by_class_name('inp-btn')

    def run(self, url):
        # kw = input('输入你要搜索的明星')
        self.send_request(url)


if __name__ == '__main__':
    douban = DouBanSpider()
    douban.run('https://movie.douban.com/')
