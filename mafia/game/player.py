#-*- encoding:utf-8 -*-

class Player:
    nickname = ''
    __socket = None
    room = None
    def __init__(self,*args,**kwargs):
        self.__socket = kwargs.pop('socket')
        pass
    def re_connected(self,*args,**kwargs):
        pass
    def leave_room(self):
        self.room.player_leave_room(self)
