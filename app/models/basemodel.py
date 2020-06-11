from datetime import datetime
from app import db


class BaseModel():
    create_time = db.Column(db.DateTime, comment='创建时间', default=datetime.now())
    update_time = db.Column(db.DateTime, comment='跟新时间', default=datetime.now(), onupdate=datetime.now())
    status = db.Column(db.Boolean, comment='是否被冻结', default=True)
