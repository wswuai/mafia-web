from app import db
from sqlalchemy.schema import Sequence

class Member(db.Model):
    username = db.Column(db.String(64), index = True, unique = True,primary_key=True)
    password = db.Column(db.String(120), index = False, unique = False)

    nickname = db.Column(db.String(64), index = False, unique = False)
    credit = db.Column(db.Integer, index = False, unique = False)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

