from app import game_server
from app import skt

from game import Player



def game_login(gameuser,gametoken,socket):
    

    for g in game_server.players:
        if g.member.username == gameuser:
            #this player is online.
            #switch connection
            g.socket = socket
            return
    
    #not online
    plyer = Player(nickname = 
    pass

def game_checkin(gameuser,gametoken):
    game_server.game_tokens[gameuser]=gametoken
