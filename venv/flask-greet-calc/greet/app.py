from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/welcome")
def Welcome():
    html='''
    <html>
    <body>
    <h1>Welcome</h1>
    <p>Welcome to my page</p>
    <a href="/welcome/home">Home</a>
    </body>
    </html>
    '''
    return 'welcome'

@app.route("/welcome/home")
def Welcome_Home():
    html='''
    <html>
    <body>
    <h1>Welcome Home</h1>
    <p>Welcome to my Home_page</p>
    <a href="/welcome/back">Leaving?</a>
    </body>
    </html>
    '''
    return "welcome home"

@app.route("/welcome/back")
def Welcome_Back():
    html='''
    <html>
    <body>
    <h1>Welcome_Back</h1>
    <p>Good to see you again</p>
    <a href="/welcome">Stay here</a>
    </body>
    </html>
    '''
    return 'welcome back'