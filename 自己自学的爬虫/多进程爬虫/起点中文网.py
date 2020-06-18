from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import requests


def send_response(url):
    response = requests.get(url)
    return response
"""
使用进程池的第一种写法
"""
# with ProcessPoolExecutor(max_workers=20) as process:
#     url_list = []
#     for i in range(1,7):
#         url = 'https://www.qidian.com/all?page={}'.format(i)
#         url_list.append(url)
#     responses = process.map(send_response,url_list)   # 第一个是要调用的函数，第二个是函数里面传的参数，必须是一个可迭代对象 返回结果的顺序的是一样的
#     for response in responses:
#         print(response)


"""
使用进程池的第二种写法
"""
with ProcessPoolExecutor(max_workers=20) as process:
    future_list = []
    for i in range(1,6):
        url = 'https://www.qidian.com/all?page={}'.format(i)
        # url_list.append(url)
        future = process.submit(send_response,url)  # 里面返回的数据的顺序不一样
        future_list.append(future)
    for i in as_completed(future_list):
        print(i.result())
