import flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import game
import gevent
from socketio.server import SocketIOServer
import json

PORT = 8000

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_MIGRATE_REPO'] = SQLALCHEMY_MIGRATE_REPO
db = SQLAlchemy(app)
skt = SocketIOServer(('0.0.0.0', PORT), app, resource="socket.io")
game_server = game.Server(name='kingdee')
######Referenced by other module

app.debug=True
skt.debug=True



#demo code
def boardcast():
    while(True):
	print("Heartbeats send")
        socketlis = [str(i) for i in skt.sockets.iteritems()]
        pkt = dict(type='heartbeat',#event
                #name='my response',
                #args=None,
                endpoint='/chat')

        for sessid, socket in skt.sockets.iteritems():
            socket.send_packet(pkt)
        gevent.sleep(1)


#gevent.spawn(boardcast)
