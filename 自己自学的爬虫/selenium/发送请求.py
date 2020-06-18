from selenium import webdriver

chrome = webdriver.Chrome(executable_path='/home/mrxu/Downloads/chromedriver')
response = chrome.get('https://www.baidu.com')
input = chrome.find_element_by_id('kw')
input.send_keys('小说')
btn = chrome.find_element_by_id('su')
response = btn.click()
chrome.page_source()




