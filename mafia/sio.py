from app import app
from flask_socketio import SocketIO, emit , send

socketio = SocketIO(app)

@socketio.on('my event')
def test_sio(message):
    print message
    emit("my response","oh, hi!, nice to meet you!")
