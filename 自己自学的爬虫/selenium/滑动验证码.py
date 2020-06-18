from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from time import sleep
from base64 import b64decode
from selenium.webdriver import ActionChains
from selenium import webdriver
import time


class BiLiSpider(object):
    def __init__(self):
        self.firefoxBinery = FirefoxBinary(firefox_path='/home/mrxu/Downloads/firefox/firefox-bin')
        self.driver = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckord0.26/geckodriver',
                                        firefox_binary=self.firefoxBinery)
        self.account = '13096575416'
        self.passwd = 'xrl000824'

    def send_request(self):
        self.driver.get('https://passport.bilibili.com/login')
        username, passwd = self.getInput()
        username.send_keys(self.account)
        passwd.send_keys(self.passwd)
        btn = self.getBtn()
        sleep(3)
        # -----------------------> 通过click点击事件
        # btn.click()

        # -----------------------> 通过执行js脚本
        # javascript = 'document.getElementsByClassName("btn btn-login")[0].click()'
        # self.driver.execute_script(javascript)

        # -----------------------> 让文本框发送enter
        username.send_keys(Keys.ENTER)
        sleep(3)
        self.get_pic()

    def get_pic(self):
        pic = ['slice_img.png','full_img.png']
        picClassName = ['geetest_canvas_bg geetest_absolute', 'geetest_canvas_fullbg geetest_fade geetest_absolute']
        for i in range(len(pic)):
            javascript = "var img = document.getElementsByClassName('" + picClassName[
                i] + "');return img[0].toDataURL('image/png');"
            print(javascript)
            info = self.driver.execute_script(javascript)
            self.write_pic(info,pic[i])


    def write_pic(self,info,file_name):
        with open('验证码图片/'+file_name,'wb') as f:
            img = info.split(',')[1]
            img_data = b64decode(img)
            print(img_data)
            f.write(img_data)


    def get_gap(self,img1,img2):
        # 返回图片的像素  0表示x轴 1表示Y轴
        print(img1.size[1],img1.size[0])
        print(img2.size[1],img2.size[0])
        left = 11
        for x_gap in range(left,img1.size[0]):
            for y_gap in range(img1.size[1]):
                if not self.is_pixel_equal(img1,img2,x_gap,y_gap):

                    left = x_gap
                    print('------------------------{}'.format(left))
                    print('------------------------{}'.format(x_gap))
                    return left

        return left

    def is_pixel_equal(self, image1, image2, x, y):
        # 获取每个像素rgb值
        pixel1 = image1.load()[x,y]  # 图片的当前坐标加载出来
        pixel2 = image2.load()[x,y]
        print(pixel1[0],pixel2[0])  # 获取图片当前坐标的R
        print(pixel1[2],pixel2[2])  # 获取图片当前坐标的G
        print(pixel1[1],pixel2[1])  # 获取图片当前坐标的B
        threshold = 10  # 阈值
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_track(self,distance):  # distance为传入的总距离
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为2
                a = 50
            else:
                # 加速度为-2
                a = -3
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self,slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹
        ActionChains(self.driver).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()


    def getInput(self):
        # selenium的显示等待
        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-username"))
        )
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-passwd"))
        )

        return username, password

    def getBtn(self):
        return self.driver.find_element_by_xpath("//a[@class='btn btn-login']")

    # 获取滑动按钮
    def get_geetest_slider_button(self):
        return self.driver.find_element_by_xpath("//div[@class='geetest_slider_button']")

    def run(self):
        self.send_request()
        img1 = Image.open('验证码图片/full_img.png')
        img2 = Image.open('验证码图片/slice_img.png')
        distance=self.get_gap(img1,img2)
        track = self.get_track(distance)
        button = self.get_geetest_slider_button()
        self.move_to_gap(button, track)
        # self.driver.quit()


if __name__ == '__main__':
    bili = BiLiSpider()
    bili.run()
