from app import app
from app import game_server
import game_service

from socketio.namespace import BaseNamespace
from socketio import socketio_manage

from flask import Response,request

#request dispatcher ( to gevent-socketio )
@app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/game': GameConnection}, request=request._get_current_object())
    except:
        app.logger.error("Exception while handling socketio connection",exc_info=True)
    return Response()



#decorator --- NEEDS CHECKIN
def needs_game_checkin(func):
    def wrapper(self,*args,**kwargs):
        if self is None:
            raise Exception("should be warpper of class function")
        gameuser = self.request.cookies.get('gameuser')
        gametoken = self.request.cookies.get('gametoken')
        tok = game_server.game_tokens.get(gameuser)
        if(tok == gametoken and tok is not None and gameuser is not None):
            func(self,*args,**kwargs)
        else:
            self.emit('connection rejected','token expired, re login!')
    return wrapper

#socket io views: --- /game
class GameConnection(BaseNamespace):
    @needs_game_checkin
    def on_req_login(self,msg):
        game_service.game_login(gameuser=self.request.cookies['gameuser'],
                                socket=self.socket)
        pass


    @needs_game_checkin
    def on_req_room_list(self,msg):
        print("on room list")
        self.emit('resp room list', [i for i in game_server.rooms])
