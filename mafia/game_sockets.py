from app import app
from app import game_server
import game_service

from socketio.namespace import BaseNamespace
from socketio import socketio_manage

from flask import Response,request
import json

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
import sys,traceback
class GameConnection(BaseNamespace):
    #decorator ----  if donot implement, crash will close socket.
    def exception_handler_decorator(self, fn):
        def wrap(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except Exception, e:
                stack = traceback.format_exception(*sys.exc_info())
                print stack
                self.emit('error',str(e))
        return wrap

    @needs_game_checkin
    def on_req_login(self,msg):
        game_service.game_login(gameuser=self.request.cookies['gameuser'], socket=self.socket)
        self.emit('resp login',{'acknowledge':True})
        pass
    @needs_game_checkin
    def on_req_room_list(self,msg):
        print("on room list")
        self.emit('resp room list', [i.__dict__ for (k,i) in game_server.rooms.viewitems()])
        print game_server.rooms
    @needs_game_checkin
    def on_req_enter_room(self,msg):
        gameuser = self.request.cookies['gameuser']
        target = json.loads(msg)
        roomname = target.roomname
        game_service.player_enter_room(gameuser,roomname)
    @needs_game_checkin
    def on_req_leave_room(self,msg):
        gameuser = self.request.cookies['gameuser']
        game_service.player_leave_room(gameuser)
    @needs_game_checkin
    def on_req_create_room(self,msg):
        username = self.request.cookies['gameuser']
        game_service.create_room(username,msg['roomname'])

    #TODO LIST
    @needs_game_checkin
    def on_chat_to_room_public(self,msg):
        #TODO
        pass

    @needs_game_checkin
    def on_order_to_room(self,msg):
        #TODO
        pass

    def on_req_server_status(self,msg):
        #TODO
        pass

    def on_chat_to_player(self,msg):
        pass
