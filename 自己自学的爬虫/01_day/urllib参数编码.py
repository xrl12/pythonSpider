import urllib.request
import urllib.parse

kw = {
    'kw': '美女'
}
# https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3
result = urllib.parse.urlencode(kw)
url = 'https://tieba.baidu.com/f?' + result
response = urllib.request.urlopen(url)
# result = response.read().decode('utf8')
with open('百度贴吧.html','wb') as f:
    f.write(response.read())
    f.close()

re = urllib.parse.unquote(result)
print(re)

