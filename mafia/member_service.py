from app import app
from app import skt
from app import db

from models import Member


def register(username,nickname,password):

    res = Member.query.filter_by(username=username).first()
    if res is not None:
        raise Exception('User exists!')

    mem = Member(username = username,nickname = nickname,password=password)
    db.session.add(mem)
    db.session.commit()

def login(username,password):
    res = Member.query.filter_by(username = username).first()
    if res is None:
        raise Exception('So Such User!')
    else:
        if res.password != password:
            raise Exception('Password Wrong!')

