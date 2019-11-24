# coding:utf-8
import os

DB_USERNAME = 'root'
DB_PASSWORD = '123456'  # 如果没有密码的话
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'spider'
DB_TYPE = 'charset=utf8'  # charset=utf8
#分页设置
PER_PAGE = 10

#SERVER_NAME = ''

DEFAULT_THEME = 'default'

CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
WEBPACK_MANIFEST_PATH = "webpack/manifest.json"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   
STATIC = os.path.join(APP_ROOT, 'static')
TEMPLATE = os.path.join(APP_ROOT, 'templates')
PUBLIC = os.path.join(APP_ROOT, 'public')


class Config:
    SECRET_KEY = os.urandom(24)  # 随机 SECRET_KEY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 自动sql

    DEBUG = True  # debug模式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)  # 数据库URL

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_POST = 25
    MAIL_USERNAME = 'm_kepler@foxmail.com'
    MAIL_PASSWORD = 'xvildlkqqkklbbbj'
    FLASK_MAIL_SUBJECT_PREFIX = 'M_KEPLER'
    FLASK_MAIL_SENDER = MAIL_USERNAME
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_DEBUG = True
    ENABLE_THREADS = True
