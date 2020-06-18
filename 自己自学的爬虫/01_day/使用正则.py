import re
#
# with open('/home/mrxu/Desktop/内涵吧1.html','r') as f:
#     data = str(f.readlines())
#     print(type(str(data)))
#
# guize = r'<div class="desc">?.*<'
# result = re.search(guize,data)
# with open('/home/mrxu/Desktop/笑话.txt','w') as f:
#     f.write(result.group())
#     f.close()
# print(result.group())


str = '123456789名字'
# 第一个传入规则 第二个传入要替换后的内容  第三个传入要替换的数据
result = re.sub(r'\d+','我是2123456',str,count=1)
print(result)