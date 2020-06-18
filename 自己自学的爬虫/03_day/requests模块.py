import requests

url = 'https://www.baidu.com'

resposne = requests.get(url)
print(resposne.content) #以字节的形式返回数据
print(resposne.text) #返回已经编码过的字符
print(resposne.url) #返回发起请求的urll
print(resposne.cookies)# 返回一个cookie
print(resposne.encoding) #返回当前的编码格式
print(resposne.headers) #返回一个请求头
print(resposne.status_code) #返回一个状态吗
resposne.encoding='utf8' #设置编码格式

"""
添加请求头
"""
heads = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            # 'Referer': 'https://www.yaozh.com/login/proxy',
        }
response = requests.get(url,heads)