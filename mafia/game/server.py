#-*- encoding:utf-8 -*-
#from room import Room
#from player import Player

class Server:
    rooms=dict()
    players=dict()
    game_tokens=dict()

    def __init__(self,*args,**kwargs):
        self.name = kwargs.pop('name')
        print 'game server is start, name=' + self.name

