from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from settings import settings

db = SQLAlchemy()
redis_db = redis.Redis(host='localhost', port=6379, db=0)


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{settings.pg_user}:{settings.pg_password}' \
        f'@{settings.pg_host}:{settings.pg_port}/{settings.db_name}'
    db.init_app(app)
