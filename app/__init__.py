from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_login import LoginManager
from flask_babelex import Babel

from config import CONFIG_MAPPING
from app.admin.modelview import ImgModelview, SkuModelview, MyModelView

db = SQLAlchemy()
loginmanager = LoginManager()  # 创建LoginManager


def create_app(config):
    app = Flask(import_name=__name__)
    app.config.from_object(CONFIG_MAPPING[config])
    db.init_app(app=app)
    # 注册版本一的接口
    from app.api import v1
    app.register_blueprint(v1)

    # 注册admin的试图
    loginmanager.login_view = 'admin.login'
    loginmanager.init_app(app=app)

    from app.admin.view import admin
    app.register_blueprint(admin)

    Migrate(app=app, db=db)

    # 注册管理后台
    admin = Admin(app, name='管理后台', template_mode='bootstrap3')  # 此行新加
    from app.models.shop import Area, ShopCategory, ShopSpu, ShopSku, ShopDetailImage, ShopGuiGeInfo, ShopGuiGeKey, \
        ShopGuiGeValue, Brank
    from app.admin.cmodelview import CatModelview
    admin.add_view(ModelView(model=Area, session=db.session, name='区域'))
    admin.add_view(CatModelview(model=ShopCategory, session=db.session, name='商品分类'))
    admin.add_view(ModelView(model=ShopSpu, session=db.session, name='商品spu'))
    admin.add_view(SkuModelview(model=ShopSku, session=db.session, name='商品sku'))
    admin.add_view(ImgModelview(model=ShopDetailImage, session=db.session, name='商品图片'))
    admin.add_view(ModelView(model=ShopGuiGeKey, session=db.session, name='商品信息键'))
    admin.add_view(ModelView(model=ShopGuiGeValue, session=db.session, name='商品信息值'))
    admin.add_view(ModelView(model=Brank, session=db.session, name='商品品牌'))
    # 对管理后台进行汉化
    babel = Babel(app=app)

    return app
