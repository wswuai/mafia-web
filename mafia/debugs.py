
from app import app
from flask import render_template

@app.route('/debug/1')
def debug1():
    return render_template("test.html")


