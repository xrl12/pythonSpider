from flask_login import login_user
from flask import Blueprint, render_template, request, redirect, url_for, flash

from .form import LoginForm
from app.models.admin import AdminUser

admin = Blueprint(name='admin_login', import_name=__name__)


@admin.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = LoginForm()
        if login.validate_on_submit():
            username = login.username.data
            pwd = login.pwd.data
            admin = AdminUser.query.filter_by(username=username, status=1).first()
            print(admin)
            if admin:
                print(admin.re_pwd(pwd=pwd))
                if admin.re_pwd(pwd=pwd):
                    login_user(admin)
                    return redirect(request.args.get('next') or url_for("admin.index"))
            flash('无效的用户名或者密码')

        return render_template('login.html', login=login)
    elif request.method == 'GET':
        login = LoginForm()
        return render_template('login.html', login=login)
