from app import game_server
#from app import skt

from game import Player
from game import Room

from models import Member



#login relative
def game_login(gameuser,socket):
    #switch socket
    for (k,g) in game_server.players.viewitems():
        if g.member.username == gameuser:
            #this player is online.
            #switch connection
            g.socket = socket
            print('socket switch, username = ' + gameuser + 'socket = '+str(g.socket))
            return

    #not online
    member = Member.query.filter_by(username=gameuser).first()
    if member is None:
        raise Exception("no member!")
    nickname = member.nickname
    plyer = Player(member=member,nickname=nickname,socket=socket)
    game_server.players[member.username] = plyer
    print ('user  online :' + member.username)
    return plyer

#important operation. be cautious to call.
def game_checkin(gameuser,gametoken):
    game_server.game_tokens[gameuser]=gametoken


#Getters...
def get_player_ins_by_name(playername):
    if playername not in game_server.players.viewkeys():
        raise Exception("Player do not exists!")
    return game_server.players[playername]


def get_room_ins_by_name(roomname):
    if roomname not in game_server.rooms.viewkeys():
        raise Exception("Room do not exists!")
    return game_server.rooms[roomname]
#room relative
def player_enter_room(playername,roomname):
    room_ins = get_room_ins_by_name(roomname)
    player_ins = get_player_ins_by_name(playername)
    if player_ins.room is not None:
        raise Exception("Player is already in room" + str(player_ins.room))

    room_ins.players[player_ins.member.username] = player_ins
    player_ins.room = room_ins

def create_room(playername,room_name,room_password=None):
    #Protection
    if room_name in game_server.rooms.viewkeys():
        raise Exception("Room Exists!")

    #new room ins
    new_room_ins = Room(name=room_name,password=room_password)
    game_server.rooms[room_name] = new_room_ins

    player_enter_room(playername,room_name)

def player_leave_room(playername):
    player_ins = get_player_ins_by_name(playername)
    if player_ins.room is None:
        raise Exception("player not in room.")

    room_ins = player_ins.room
    player_ins.room = None
    room_ins.players.pop(playername)
    if len(room_ins.players)==0:
        game_server.rooms.pop(room_ins.name)
        print("room is empty, delete")

def chat_to_room_public(player):
    #TODO
    pass


def order_to_room(player,order):
    #TODO
    pass
