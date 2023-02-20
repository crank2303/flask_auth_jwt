from functools import wraps

import jwt
from flask import Flask, request, jsonify
from flask_redoc import Redoc
from werkzeug.security import generate_password_hash

from db import db, init_db
from db_models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['REDOC'] = {
    'spec_route': '/docs',
    'title': 'Flask Auth Service',}

redoc = Redoc(app, 'service.yml')
# Подготоваливаем контекст и создаём таблицы
init_db(app)
app.app_context().push()
db.create_all()


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


@app.route('/register', methods=['GET', 'POST'])
def signup_user():
    # data = request.get_json()
    hashed_password = generate_password_hash("sddad", method='sha256')

    new_user = User(login="dasda", password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'registered successfully'})


@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
