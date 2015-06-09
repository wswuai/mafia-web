#-*- encoding:utf-8 -*-

class Player:
    nickname = ''
    member = None
    socket = None
    room = None
    def __init__(self,*args,**kwargs):
        self.socket = kwargs.pop('socket')
        self.nickname = kwargs.pop('nickname')
        self.member = kwargs.pop('member')
        self.room = None
        pass
    def re_connected(self,*args,**kwargs):
        pass
    def leave_room(self):
        self.room.player_leave_room(self)

    def __str__(self):
        return "<PLAYER : nickname=%s, member=%s, socket=%s, room=%s>" % (self.nickname,self.member,self.socket,self.room)
