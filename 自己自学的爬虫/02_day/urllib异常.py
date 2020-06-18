import urllib.request
from urllib.error import URLError, HTTPError

url = 'https://www.baidu.com/234'
try:
    result = urllib.request.urlopen(url)

except HTTPError as errof:
    print(errof.code)
    print(errof.reason)
    print(errof.headers)

except URLError as error:
    print(error.reason)
