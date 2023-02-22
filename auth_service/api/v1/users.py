from http import HTTPStatus

from database.service import create_user
from database.models import Users
from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash


def register_new_user():
    name = request.values.get('login', None)
    password = request.values.get('password', None)
    if not name or not password:
        return make_response('Username or password is empty', HTTPStatus.BAD_REQUEST)
    db_username = Users.query.filter_by(login=name).first()
    if db_username:
        return make_response('Username is already exist', HTTPStatus.BAD_REQUEST)
    create_user(name, password)
    return jsonify(msg=f'Account {name} was successfully registered')


def login_user():
    name = request.values.get('login', None)
    password = request.values.get('password', None)
    if not name or not password:
        return make_response('Username or password is empty', HTTPStatus.BAD_REQUEST)
    db_account = Users.query.filter_by(login=name).first()
    if not db_account:
        return make_response('Username does not exist', HTTPStatus.BAD_REQUEST)
    correct_password = check_password_hash(db_account.password, password)
    if not correct_password:
        return make_response('Incorrect password', HTTPStatus.BAD_REQUEST)
    else:
        return 'Authorization is successful!'
