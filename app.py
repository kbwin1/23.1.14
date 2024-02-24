# Put your app in here.
from flask import Flask
from flask import request
app=Flask(__name__)


@app.route('/add<int:a>+<int:b>')
def add(a,b):
    c=a+b
    return f"Result: {c}"


@app.route('/sub<int:a>-<int:b>')
def sub(a,b):
    c=a-b
    return f"Result: {c}"


@app.route('/mult<int:a>*<int:b>')
def mult(a,b):
    c=a*b
    return f"Result: {c}"


@app.route('/div<int:a>/<int:b>')
def div(a,b):
    c=a/b
    return f"Result: {c}"