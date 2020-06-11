from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField(label='用户名字', validators=[DataRequired('请填写住账号')])
    pwd = PasswordField(label='密码', validators=[DataRequired('请填写密码')])
    ok = SubmitField(label='登录')
