#-*- encoding:utf-8 -*-

class Player:
    nickname = ''
    member = None
    token = None
    socket = None
    room = None
    def __init__(self,*args,**kwargs):
        self.socket = kwargs.pop('socket')
        self.nickname = kwargs.pop('nickname')
        self.member = kwargs.pop('member')
        self.token = kwargs.pop('token')
        self.room = None
        pass
    def re_connected(self,*args,**kwargs):
        pass
    def leave_room(self):
        self.room.player_leave_room(self)