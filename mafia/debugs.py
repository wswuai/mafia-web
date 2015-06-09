
from app import app
from flask import render_template
from app import game_server
from app import skt
import game_service
import game




@app.route('/debug/1')
def debug1():
    return render_template("test.html")


@app.route('/eval/<cmd>')
def debugeval(cmd):
    try:
        return eval(cmd)
    except Exception,e:
        return e
