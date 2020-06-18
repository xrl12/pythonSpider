import urllib.request
import urllib.parse
import json


class LaGo(object):
    def __init__(self, page):
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        self.heads = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content - Length': '25',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
            'Cookie': 'JSESSIONID=ABAAABAABGGAAFD1C7AE8423D6BC8650553E83BB38623D3; user_trace_token=20200305210906-85ab0132-c5ad-4518-8e94-2e0283cff630; WEBTJ-ID=03052020%2C050902-170aad04b88f5-0852658cadd65c-317d0e5e-1703184-170aad04b8a3f1; LGUID=20200305210907-3639d9f3-a2bd-4584-8d25-96319e7396ed; _ga=GA1.2.1816939917.1583413743; sajssdk_2015_cross_new_user=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1583413743; _gid=GA1.2.575393611.1583413743; LGSID=20200305214825-b3c3b43c-b7fc-48d7-97a0-257b979e1297; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170aad04e2043f-0941f95929278b-317d0e5e-1703184-170aad04e21685%22%2C%22%24device_id%22%3A%22170aad04e2043f-0941f95929278b-317d0e5e-1703184-170aad04e21685%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24os%22%3A%22Linux%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2280.0.3987.132%22%7D%7D; X_MIDDLE_TOKEN=d0a9fb64ba74fead4b61e16f634639f9; _gat=1; X_HTTP_TOKEN=713e56902a22615e8888143851c6030b10daa233fc; SEARCH_ID=e36d5bb88ad8408987342f56038bef3b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1583418899; LGRID=20200305223459-8bf1d303-35d1-4777-b4fe-235fa8e9343f',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',  # 表示从那个页面进来的
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest',
        }
        # 创建post请求的参数
        self.form_data = {
            'first': 'true',
            'pn': page,
            'kd': 'python'
        }
        self.json = []
        print('我正在发送第{}次请求'.format(page))

    def get_request(self, form_data):
        form_data1 = urllib.parse.urlencode(form_data).encode('utf8')
        url = urllib.request.Request(url=self.url, data=form_data1, headers=self.heads)
        response = urllib.request.urlopen(url)
        return response

    def parse(self, content):
        data = content.read().decode('utf8')
        if not self.json:
            self.json = json.loads(data)
            print(bool(not self.json))
        else:
            self.json['content']['positionResult'] = self.json['content']['positionResult'] + data.get('content').get(
                'positionResult').get('result')
            # print(self.json)
            # self.json = json.dumps(self.json)
            self.write_file(self.json)



    def write_file(self, content):
        with open('/home/mrxu/PycharmProjects/WangLulZhiZhu/02_day/拉钩.json', 'a') as f:
            f.write(content)
            f.close()

    def start(self):
        content = self.get_request(self.form_data)
        self.parse(content)


if __name__ == '__main__':
    for i in range(1, 3):
        lago = LaGo(i)
        lago.start()
