from .basemodel import BaseModel
from app import db


class Area(BaseModel, db.Model):
    __tablename__ = 'area'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False, default='', comment='区域：比如，发现好物')
    position = db.Column(db.Integer(), nullable=False, default=1, comment='所在在位置是否考前')


# 商品分类
class ShopCategory(BaseModel, db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, default='', unique=True)
    position = db.Column(db.Integer(), nullable=False, default=1)
    show_page = db.Column(db.Integer(), nullable=False, default=2)  # 1是首页，2是发现好物页

    area_id = db.Column(db.Integer(), nullable=False, default=0, comment='属于那个区域的')
    own = db.Column(db.Integer(), nullable=False, default=0, comment='二级分类进关联一级分类')


# 商品品牌
class Brank(BaseModel, db.Model):
    __tablename__ = 'brank'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False, default='', comment='品牌')
    first_letter = db.Column(db.String(32), nullable=False, comment='品牌的首字母')
    logo = db.Column(db.String(200), nullable=False, comment='logo图片链接')


# 商品里面的属性是一样的
class ShopSpu(BaseModel, db.Model):
    __tablename__ = 'shopspu'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False, default='', comment='商品名字')
    sales = db.Column(db.Integer(), nullable=False, default=0, comment='销量')
    comments = db.Column(db.Integer(), nullable=False, default=0, comment='评论数量')
    desc_detail = db.Column(db.String(100), nullable=False, default='', comment='商品详情')
    desc_pack = db.Column(db.String(100), nullable=False, default='', comment='包装信息')
    desc_server = db.Column(db.String(100), nullable=False, default='', comment='售后服务')
    ishot = db.Column(db.Boolean(), nullable=False, default=False, comment='是否在主页显示')

    cid = db.Column(db.Integer, nullable=False, default=0, comment='分类ID')
    brand_id = db.Column(db.Integer(), nullable=False, comment='品牌ID')


# 商品里面的属性不一样
class ShopSku(BaseModel, db.Model):
    __tablename__ = 'shopsku'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, comment='主键，唯一标识')
    name = db.Column(db.String(32), nullable=False, default='', comment='sku的名字')
    price = db.Column(db.DECIMAL(8, 2), nullable=False, comment='商品的售价', default=0)
    cost_price = db.Column(db.DECIMAL(8, 2), nullable=False, comment='商品的进价', default=0)
    market_price = db.Column(db.DECIMAL(8, 2), nullable=False, comment='商品的市场价', default=0)
    stock = db.Column(db.Integer(), nullable=False, default=0, comment='库存')
    salas = db.Column(db.Integer(), nullable=False, default=0, comment='销量')
    comments = db.Column(db.Integer, nullable=False, default=0, comment='评论量')
    is_launched = db.Column(db.Boolean, nullable=False, default=True, comment='是否上架')
    default_img_url = db.Column(db.String(100), nullable=False, default='', comment='主页图片的路由')

    shop_id = db.Column(db.Integer, nullable=False, default=0, comment='进行关联的商品的id')


# 商品的详情图
class ShopDetailImage(BaseModel, db.Model):
    __tablename__ = 'shopdetailimage'
    id = db.Column(db.Integer, primary_key=True, comment='唯一标示', autoincrement=True)
    img = db.Column(db.String(100), nullable=False, default='', comment='详情图的url地址')

    shop_spu_id = db.Column(db.Integer, nullable=False, default='', comment='所关联的商品')


# 商品规格的键
class ShopGuiGeKey(BaseModel, db.Model):
    __tablename__ = 'shopguigekey'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, comment='主键，唯一标识')

    shop_id = db.Column(db.Integer, nullable=False, default=0, comment='商品的主键,')
    name = db.Column(db.String(32), nullable=False, default='', comment='商品属性的名字')


# 商品规格的值
class ShopGuiGeValue(BaseModel, db.Model):
    __tablename__ = 'shopguigevalue'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, comment='主键，唯一标识')
    value = db.Column(db.String(32), nullable=False, default='', comment='属性值')

    key_id = db.Column(db.Integer, nullable=False, default=0, comment='商品规格的键进行关联')


# 规格信息
class ShopGuiGeInfo(BaseModel, db.Model):
    __tablename__ = 'shopguigeinfo'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, comment='主键，唯一标识')

    sku_id = db.Column(db.Integer, nullable=False, default=0, comment='商品sku的id')
    guigekey = db.Column(db.Integer, nullable=False, default=0, comment='商品规格的键的ID')
    guigevlaue = db.Column(db.Integer, nullable=False, default=0, comment='商品规格值的ID')
