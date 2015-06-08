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

    ### checkin user to game server

    
    resp.set_cookie('gameuser',username)
    import hashlib
    import time
    tok = hashlib.sha1(str(time.time())).hexdigest()
    resp.set_cookie('gametoken',tok)

    game_service.game_checkin(username,tok)
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
