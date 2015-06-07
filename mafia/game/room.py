#-*- encoding:utf-8 -*-
from player import Player

class Room:
    name = ''
    players = set()
    password = None
    game_time = dict()
    status = 'AWAIT' # other wise, 'PLAYING'
    def __init__(self,*args,**kwargs):
        self.name = kwargs.pop('name')
        self.password = kwargs.pop('password',None)
        self.game_time = dict()
        self.status = 'AWAIT'
    
    def player_leave_room(self,player):
        #terms
        if player not in self.players:
            raise Excepton('cannot find player')

        #process
        self.players.remove(player)
        player.room = None

    def enter(self,player):
        if player.room is not None:
            player.leave_room()

        self.players.add(player)
        player.room = self

if __name__=='__main__':
    a = Room(name='new room!', password='***')
    p = Player(nickname='p1',socket=None)
    a.enter(p)
    p.leave_room()


