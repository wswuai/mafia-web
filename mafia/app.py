import flask
import game
import gevent
from socketio.server import SocketIOServer
import json

app = flask.Flask(__name__)
PORT = 8000
app.debug=True
skt = SocketIOServer(('0.0.0.0', PORT), app, resource="socket.io")
skt.debug=True

game_server = game.server(name='kingdee')


def boardcast():
    while(True):

        socketlis = [str(i) for i in skt.sockets.iteritems()]

        pkt = dict(type='event',
                name='my response',
                args=[json.dumps(socketlis)],
                endpoint='/chat')

        print 'gcnt=' + str(global_cnt)

        for sessid, socket in skt.sockets.iteritems():
            socket.send_packet(pkt)
            #socket['/chat'].emit('my response','hi?')
        gevent.sleep(1)


#gevent.spawn(boardcast)
