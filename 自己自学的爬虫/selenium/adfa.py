from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import base64
from PIL import Image


class BiLiSpider():
    def __init__(self):
        self.firefoxBinery = FirefoxBinary(firefox_path='/home/mrxu/Downloads/firefox/firefox-bin')
        self.driver = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckord0.26/geckodriver',
                                        firefox_binary=self.firefoxBinery)
        self.username = '13096575416'
        self.password = 'xrl000824'
        self.url = 'https://passport.bilibili.com/login'

    # 发起请求
    def send_request(self):
        self.driver.get(url=self.url)

    # 找账号和密码的输入框
    def get_input(self):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "login-username"))
        )
        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "login-passwd"))
        )
        return username, password

    # 找登录按钮
    def get_btn(self):
        btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-login"]'))
        )
        return btn

    # 通过js获取图片

    def get_pic(self):
        picName = ['full.png', 'slice.png']
        className = ['geetest_canvas_fullbg', 'geetest_canvas_bg']
        for i in range(len(className)):
            js = "var change = document.getElementsByClassName('" + className[
                i] + "'); return change[0].toDataURL('image/png');"
            im_info = self.driver.execute_script(js)  # 执行js叫吧
            self.save_pic(im_info, picName[i])

    # 解码保存成图片
    def save_pic(self, data, filename):
        print(data)
        data = data.split(',')[1]
        data = base64.b64decode(data)
        with open(filename, 'wb') as f:
            f.write(data)

    def get_gap(self, img1, img2):
        print(img1.size[0], img1.size[1])
        left = 10
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    # 根据像素xy坐标判断红绿蓝是否一样
    def is_pixel_equal(self, image1, image2, x, y):
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        print(pixel1)
        print(pixel2)
        threshold = 40  # 阈值
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_track(self, distance):
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 因为老对不的不准确，所以自行调整一下distance
        distance = distance - 9
        # 减速阈值 也就是加速到什么位置的时候开始减速
        mid = distance * 4 / 10
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 200
            else:
                # 加速度为负3
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t  # 位移公式
            current += move
            print(round(move))
            track.append(round(move))
        print(track)
        return track

    # 获取要移动的按钮
    def get_slider_button(self):
        ''
        sliderbutton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='geetest_slider_button']"))
        )
        return sliderbutton

    def move_to_gap(self, slider, tracks):
        # click_and_hold()点击鼠标左键，不松开
        ActionChains(self.driver).click_and_hold(slider).perform()
        for x in tracks:
            # move_by_offset()鼠标从当前位置移动到某个坐标
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        # release()在某个元素位置松开鼠标左键
        ActionChains(self.driver).release().perform()

    def start(self):
        self.send_request()
        username, password = self.get_input()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(3)

        btn = self.get_btn()
        btn.click()

        time.sleep(1)
        self.get_pic()

        # 算距离
        img1 = Image.open('full.png')
        img2 = Image.open('slice.png')

        # 获取移动的距离
        left = self.get_gap(img1, img2)

        # 计算位移

        track = self.get_track(left)
        slider = self.get_slider_button()
        # 开始移动
        self.move_to_gap(slider, track)


if __name__ == '__main__':
    bls = BiLiSpider()
    bls.start()
