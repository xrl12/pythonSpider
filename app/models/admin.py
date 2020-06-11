from flask_login import UserMixin
from app import db
from app.models.basemodel import BaseModel
from app import loginmanager
from app.util.tools import get_md5


class AdminUser(db.Model, BaseModel,UserMixin):
    __tablename__ = 'AdminUser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), comment='员工名字')
    group = db.Column(db.String(32), comment='员工是那个部门的')
    password = db.Column(db.String(100), comment='登录密码')

    def re_pwd(self, pwd):
        pwd = get_md5(str=pwd)
        return self.password == pwd


@loginmanager.user_loader
def load_user(userid):
    user = AdminUser.query.filter_by(id=userid).first()
    return user
