import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from .postgresql import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    login = db.Column(
        db.String,
        unique=True,
        nullable=False,
    )
    password = db.Column(
        db.String,
        nullable=False,
    )

    def __repr__(self):
        return f'<User {self.login}>'


class AuthLogs(db.Model):
    __tablename__ = 'auth_logs'

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = db.Column(
        UUID(as_uuid=True),
        ForeignKey(Users.id),
    )
    user_agent = db.Column(
        db.String,
        nullable=False,
    )
    log_type = db.Column(
        db.String,
        nullable=True,
    )
    datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now()
    )
    ip_address = db.Column(
        db.String,
        nullable=True,
    )


class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = db.Column(
        db.String,
        unique=True,
        nullable=False,
    )

    def __repr__(self):
        return f'<Roles {self.name}>'


class UsersRoles(db.Model):
    __tablename__ = 'users_roles'

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = db.Column(
        UUID(as_uuid=True),
        ForeignKey(Users.id),
    )
    role_id = db.Column(
        UUID(as_uuid=True),
        ForeignKey(Roles.id),
    )
