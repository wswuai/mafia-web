#-*- encoding:utf-8 -*-
from room import Room
from player import Player

class Server:
    rooms=set()
    players=set()

    def __init__(self,*args,**kwargs):
        self.name = kwargs.pop('name')
        print 'game server is start, name=' + self.name
        self.players = kwargs.pop('players',[])

    def create_room(self,new_room):
        #assert terms:
        for room in self.rooms:
            if (room.name == new_room.name):
                raise Exception('Room Name Conflict')
        #create new room:
        self.rooms.add(new_room)
        print("room created, ins >>", new_room)
        print("room list:", str(self.room_list))

    def delete_room(self,target_room):
        if target_room not in self.rooms:
            raise Exception('no such room')

        self.rooms.remove(target_room)

    def room_list(self):
        return self.rooms

    def player_enter_room(self,player,target_room):
        #limit terms:
        if target_room not in self.rooms:
            raise Exception('room do not exists')
        
        #processing:
        target_room.enter(player)

    def player_login(self,player):
        self.player.add(player)



#test
if __name__=='__main__':
    server = Server(name='kd')
    r1 = server.create_room(Room(name='hello'))
    server.create_room(Room(name='hello1'))
    server.create_room(Room(name='hello2'))
    server.create_room(Room(name='hello3'))
    server.create_room(Room(name='hello5'))
    server.create_room(Room(name='hello4'))
    print 'room list:'
    for i in server.room_list():
        print i.name

    del_list = [i for i in server.room_list()]
    #for i in del_list:
    #    server.delete_room(i)

 
    plyer = Player(name='1',socket=None)
    server.player_enter_room(plyer,r1)

    print '(after delete) room list:'
    for i in server.room_list():
        print i.name

   
