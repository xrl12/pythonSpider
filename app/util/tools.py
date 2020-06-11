import string
import random


def get_sal(size):
    """
    :param size: 获取多少为的随机值
    :return:  返回一个随机值
    """
    salt = [random.choice(string.ascii_letters + string.digits) for _ in range(1, size + 1)]
    return ''.join(salt)


import hashlib


# 生成一个md5加密值
def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf8'))
    return md5.hexdigest()


def get_token(openid, salt):
    """
    :param openid 从微信后台返回来的值，确保token的唯一性
    :param salt: 一个唯一值，确保token的唯一性
    :return:  token
    """
    value = str(salt) + str(openid)
    token = get_md5(value)
    return token
