from app import game_server
from app import skt

from game import Player

import member_service
from models import Member


def game_login(gameuser,gametoken,socket):
    #validate
    tok = game_server.game_tokens.get(gameuser)
    if tok is None or gametoken != tok:
        raise Exception('game login failed: Token donot fit')

    #switch socket
    for g in game_server.players:
        if g.member.username == gameuser:
            #this player is online.
            #switch connection
            g.socket = socket
            print('socket switch, username = ' + gameuser)
            return

    #not online
    print ('user not online, try to get online')
    member = Member.query.filter_by(username=gameuser)
    nickname = member.nickname
    token = gametoken
    plyer = Player(member=member,nickname=nickname,token=token)
    game_server.player_login(plyer)
    print ('user  online :' + member.username)
    return plyer

#important operation. be cautious to call.
def game_checkin(gameuser,gametoken):
    game_server.game_tokens[gameuser]=gametoken

