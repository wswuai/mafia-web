from app import app
from app import game_server

from socketio.namespace import BaseNamespace
from socketio import socketio_manage

from flask import Response,request
@app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/chat': GameConnection}, request=request._get_current_object())
    except:
        app.logger.error("Exception while handling socketio connection",
                         exc_info=True)
    return Response()


class GameConnection(BaseNamespace):
    def on_my_event(self,msg):
        #print self.socket
        #self.request << get session stuff.
        #self.emit('my response', str(self.request.cookies))
        self.emit('my response', str([i for i in self.socket.server.sockets.iteritems()]))
        pass

    def on_login_req(self,msg):
        pass

    def on_room_list(self,msg):
        pass

