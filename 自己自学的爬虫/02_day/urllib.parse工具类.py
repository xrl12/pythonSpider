import urllib.parse

# 一个url的组成
"""
url = https://book.qidian.com/info/1017777013#Catalog
由协议 https
域名 book.qidian.com
端口 一般不显示
路径 info/1017777013
参数 ?age=20
锚点 #Catalog
"""

# 把一个完成的url给切割开来 allow_fragments为true是不忽略锚点，如果为False就会忽略锚点
# url = 'https://book.qidian.com/info/1017777013#Catalog'
# result = urllib.parse.urlparse(url=url,allow_fragments=False)
# print(result)
# print(result.scheme)
# print(result.fragment)
# print(result.netloc)
# print(result.path)
# print(result.params)
# print(result.query)
#
# # 把一个切割的路由进行拼装起来
# url = ('https','book.qidian.com','/info/1017777013','','','Catalog')
# result = urllib.parse.urlunparse(url)
# print(result)


# # 进行拼装路由
# baseurl = 'https://book.qidian.com/info/1017777013#Catalog'
# suburl = 'info/1018368514'
# result = urllib.parse.urljoin(baseurl,suburl)
# print(result)


# 对中文进行编码
kw = '徐瑞鑫是个灵才才'
result = urllib.parse.quote(kw)
print(result)

# 对中文进行编码
kw = {
    'name': '徐瑞鑫',
    'age': 12,
    'gender':'男',
    'address':"山西省忻州市五寨县"
}
result = urllib.parse.urlencode(kw)
print(result)
