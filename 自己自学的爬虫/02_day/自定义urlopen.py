import urllib.request


url = 'http://www.baidu.com'
# 创建一个HTTPHandler
http_handler = urllib.request.HTTPHandler()
# 创建一个build_opener传入一个http_handler
build_opener = urllib.request.build_opener(http_handler)

response = build_opener.open(url)
print(response.getcode())
print(response.status)
print(response.info())
print(response.geturl())

