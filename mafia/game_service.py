from app import game_server
from app import skt

from game import Player

from models import Member


def game_login(gameuser,socket):
    #switch socket
    for g in game_server.players:
        if g.member.username == gameuser:
            #this player is online.
            #switch connection
            g.socket = socket
            print('socket switch, username = ' + gameuser + 'socket = '+str(g.socket))
            return

    #not online
    member = Member.query.filter_by(username=gameuser).first()
    nickname = member.nickname
    plyer = Player(member=member,nickname=nickname,socket=socket)
    game_server.player_login(plyer)
    print ('user  online :' + member.username)
    return plyer

#important operation. be cautious to call.
def game_checkin(gameuser,gametoken):
    game_server.game_tokens[gameuser]=gametoken

