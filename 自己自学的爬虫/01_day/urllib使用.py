import urllib.request
import os

url = 'http://www.baidu.com'

"""
字节转换字符串：使用decode方法
字符串转换字节：使用enconde方法
"""


def text_create(name, msg):
    full_path = '/home/mrxu/Desktop' + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)   #msg也就是下面的Hello world!
    file.close()
def mkdocu(name,data):
    path = '/home/mrxu/Desktop/' + name +'.txt'
    file = os.open(path,os.O_CREAT|os.O_WRONLY)
    os.write(file,str.encode(data))
    os.close(file)

response = urllib.request.urlopen(url)

print(response.info())   # 响应头里面的数据
print(response.status)   # 状态码
print(response.getcode())  # 状态码
print(response.geturl())   # 获取当期路径

"""
response.read()只可以读一次   
"""
# 读取出response里面的信息，返回的是字节
document = response.read().decode('utf8')

mkdocu('百度',document)

