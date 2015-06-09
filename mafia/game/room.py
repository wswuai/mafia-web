#-*- encoding:utf-8 -*-
from player import Player
import json

class Room:
    name = ''
    players = dict()
    password = None
    game_time = dict()
    rules = None
    status = 'AWAIT' # other wise, 'PLAYING'
    def __init__(self,*args,**kwargs):
        self.name = kwargs.pop('name')
        self.password = kwargs.pop('password',None)
        self.rules = kwargs.pop('rules',None)
        self.game_time = dict()
        self.status = 'AWAIT'
    def __dict__(self):
        res = {}
        res['name'] = self.name
        res['players'] = [p.__dict__ for p in self.players]
        res['game_time'] = self.gametime
        res['rules'] = self.rules
        res['status'] = self.status
        return res


if __name__=='__main__':
    a = Room(name='new room!', password='***')
    p = Player(nickname='p1',socket=None)
    a.enter(p)
    p.leave_room()


