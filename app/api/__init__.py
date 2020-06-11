from flask import Blueprint
from .v1 import user
from .v1 import shop

v1 = Blueprint(name='v1', import_name=__name__)
user.api.register(v1, url_prefix='/api/v1/')
shop.shop.register(v1,url_prefix='/api/v1/')