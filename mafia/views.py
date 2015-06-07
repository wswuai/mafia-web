from app import app
from app import skt
from flask import render_template, Response, request ,session, make_response
import socketio
from socketio import socketio_manage
from socketio import gevent
from sio import MafiaNameSpace
import json
import copy

@app.route("/")
def index():
    for i in skt.sockets.iteritems():
        print i
    resp = make_response(render_template("index.html"))
    resp.set_cookie('userid','^!@Dfqwi')
    return resp

@app.route('/boardcast')
def bc():

    pkt = dict(type='event',
            name='my response',
            args='cool',
            endpoint='/chat')

    for sess,socket in skt.sockets.iteritems():
        #socket.emit('my response','hi theeere!')
        socket.send_packet(pkt)
        print sess,socket
    return "well?"

@app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/chat': MafiaNameSpace}, request=request._get_current_object())
    except:
        app.logger.error("Exception while handling socketio connection",
                         exc_info=True)
    return Response()

def infinite():
    for i in range(0,10):
        gevent.sleep(1)
        print("awake!")

@app.route('/gspawn')
def gspawn():
    gevent.spawn(infinite)
    return "spawnedd"

