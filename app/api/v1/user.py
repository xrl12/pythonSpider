import requests
from flask import current_app, jsonify

from app import db
from app.util.redprint import Redprint
from app.models.user import Member, OauthMemberBind
from app.models.shop import *
from app.util.tools import get_sal,get_token
api = Redprint(name='user')


@api.route('', methods=['POST', 'GET'])
def login(code, nickname, avatarUrl, gender, ip):
    """
    :param code: 从微信后台传过来的
    :param nickname 用户的昵称
    :param avatarUrl 用户头像的url
    :param gender 用户性别 0：未知、1：男、2：女
    :param ip 用户ip地址
    :return:  Token  （登录唯一标示）
    """
    ctx = {
        'code': 1,
        'msg': 'ok',
        'data': {}
    }
    appid = current_app.config['APPID']
    APPSECRET = current_app.config['APPSECRET']
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={appsecret}&js_code={code}&grant_type=authorization_code'.format(
        appid=appid, appsecret=APPSECRET, code=code
    )
    response = requests.get(url).json()

    if response == '-1':
        ctx['code'] = -1
        ctx['msg'] = '系统繁忙，请稍等在登录'
        return jsonify(ctx)

    elif response == '40029':
        ctx['code'] = 40029
        ctx['msg'] = '参数错误'
        return jsonify(ctx)

    elif response == '45011':
        ctx['code'] = 45011
        ctx['msg'] = '你登录次数过多'
        return jsonify(ctx)

    elif response == '0':
        openid = response.get('openid')
        session_key = response.get('session_key')
        unionid = response.get('unionid')
        salt = get_sal(32)
        member = Member()
        member.reg_ip = ip
        member.nickname = member.nickname
        member.gender = gender
        member.avatar = avatarUrl
        member.salt = salt
        db.session.add(member)
        db.session.commit()

        oauthmember = OauthMemberBind()
        oauthmember.openid = openid
        oauthmember.client_type = '微信'
        oauthmember.type = 1
        oauthmember.unionid = unionid
        oauthmember.session_key = session_key
        oauthmember.member_id = member.id
        db.session.add(oauthmember)
        db.session.commit()

        return get_token(salt=salt,openid=openid)

    else:
        ctx['code'] = -1
        ctx['msg'] = '参数错误'
        return jsonify(ctx)
