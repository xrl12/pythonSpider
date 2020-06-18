import urllib.request
import urllib.parse
import ssl


# 发送post请求


# 有道的一个老接口
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
#构建表单数据 要对数据进行编码 转换为unicode类型
formdata = {
    'i': '你好',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}

UA = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
}
result = urllib.parse.urlencode(formdata).encode('utf8')
full_url = urllib.request.Request(url=url,data=result,headers=UA)
response = urllib.request.urlopen(full_url)
print(response.getcode())
print(response.read())

