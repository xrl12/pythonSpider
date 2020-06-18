from selenium import webdriver

river = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckodriver')
river.get('https://movie.douban.com/')