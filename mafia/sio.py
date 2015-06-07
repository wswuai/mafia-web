from app import app

from socketio.namespace import BaseNamespace



class MafiaNameSpace(BaseNamespace):
    def on_my_event(self,msg):
        #print self.socket
        #self.request << get session stuff.
        self.emit('my response', str(self.request.cookies))
        pass

    def on_login_req(self,msg):
        pass

    def on_room_list(self,msg):
        pass

