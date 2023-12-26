from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(18), nullable=False)


class RevokedTokensModel(db.Model):
    __tablename__ = "revoked_token"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, unique=True, nullable=False)
    deleted_at = db.Column(db.String, nullable=False)