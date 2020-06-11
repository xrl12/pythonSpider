import pymysql
from flask_migrate import Manager, MigrateCommand, Migrate

from app import create_app
pymysql.install_as_MySQLdb()
app = create_app(config='dev')
manage = Manager(app=app)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()
