import re
#
with open('/home/mrxu/Desktop/笑话.txt', 'r') as f:
    data = f.readlines()
    str = ''.join(data)
    print(str)
    ret = re.compile(r'<div class="desc">(\D*?)<.*?>')

    result = ret.findall(str)
    print(result)
    # str2 = ''.join(result)
    # print(str2)
    # with open('/home/mrxu/Desktop/笑话.txt','w+') as d:
    #     d.write(str2)
    #     print('这是字符串2',str2)
    #     print('这是存进去的',f.readlines())
    #     d.close()
    f.close()

