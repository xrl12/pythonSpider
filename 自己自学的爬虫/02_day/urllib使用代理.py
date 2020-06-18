import urllib.request

# 使用免费代理
proxies = {
    'HTTP': '27.11.205.43:8118',
    'HTTP': '120.132.116.81:8080'
}
url = 'http://www.baidu.com'
proxy_handler = urllib.request.ProxyHandler(proxies=proxies)
bulid_opener = urllib.request.build_opener(proxy_handler)
response = bulid_opener.open(url)
print(response.status)
print(response.info())

urllib.request.urlopen()

# 使用付费代理
# 购买代理后，会给一个账号和密码
proxies = {
    'HTTP': 'accout:passwd@ip:端口'
}
url = 'http://www.baidu.com'
proxy_handler = urllib.request.ProxyHandler(proxies=proxies)
bulid_opener = urllib.request.build_opener(proxy_handler)
response = bulid_opener.open(url)
print(response.status)
print(response.info())