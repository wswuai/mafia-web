from app import game_server
from app import app
from app import skt

from game.player import Player
import game_service
import game_sockets
import member_service





player = Player()

game_service.chat_to_room_public(player)
