import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from core.settings import settings

db = SQLAlchemy()
SQLALCHEMY_DATABASE_URI = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.pg_host}:{settings.pg_port}/{settings.postgres_db}"


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    
