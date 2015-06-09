#from app import game_server
import game_service


def send_event_socket(socket, event, *args, **kwargs):
    pkt = dict(type="event", name=event, args=args, endpoint='/game')
    socket.send(pkt)

def send_event_player(username,event,*args,**kwargs):
    player_ins = game_service.players[username]
    send_event_socket(player_ins.socket,event,*args,**kwargs)

def send_chat_content_public(room_ins, content):
    for player in room_ins.players:
        send_event_player('chat public', content)

def send_chat_content_private(player_ins, target_player_ins, content):
    send_event_player(target_player_ins.socket,'chat private', {'from':player_ins.nickname, 'content':content})


