from app import app
from app import skt
from app import db
#App Manipulate stub
import member_service
import game_service

from flask import render_template, Response, request ,session, make_response, jsonify,redirect,url_for,abort




@app.route("/")
def index():
    gameuser = request.cookies.get('gameuser')
    if gameuser is not None:
        pass
        
    resp = render_template("index.html")
    return resp


@app.route("/login",methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    if None in [username,password]:
        return jsonify( {'result':'Wrong Params'} )
    
    try:
        member_service.login(username,password)
    except Exception,e:
        abort(401)
    #ok.then.

    resp = make_response(jsonify({'status':True}))
    #resp = make_response('hi')
    ### set user to game server
    
    resp.set_cookie('gameuser',username)
    resp.set_cookie('gametoken','FLSKF:I@#*RY*@Y*YR)B')
    return resp
    

@app.route("/register",methods=['POST'])
def register():
    username = request.form.get('username')
    nickname = request.form.get('nickname')
    password = request.form.get('password')
    if None in [username,nickname,password]:
        abort(401)
    try:
        member_service.register(username=username,nickname=nickname,password=password)
    except Exception,e:
        abort(401)
    return redirect('index')

#Socket IO Interface

#from socketio import socketio_manage
#from game_sockets import GameConnection
#@app.route('/socket.io/<path:remaining>')
#def socketio(remaining):
#    try:
#        socketio_manage(request.environ, {'/chat': GameConnection}, request=request._get_current_object())
#    except:
#        app.logger.error("Exception while handling socketio connection",
#                         exc_info=True)
#    return Response()
#
#
##@app.route('/login')
