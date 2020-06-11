class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/xingjilegou'

    # 数据库和模型类同步修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = False

    # 小程序的APPID
    APPID = 'wxe0632a1e3ec5281f'
    APPSECRET = '6970027d6bb20698cfc20561d4dee03d'


    # 配置session
    SECRET_KEY = 'ADSAFDSFADSFASDFADSFADSFDSFS'

    # 对管理后台进行汉化
    BABEL_DEFAULT_LOCALE = 'zh_CN'


# 开发
class Dev(Config):
    DEBUG = True


# 　上线
class Pro(Config):
    DEBUG = False


CONFIG_MAPPING = {
    'dev': Dev,
    'pro': Pro
}
