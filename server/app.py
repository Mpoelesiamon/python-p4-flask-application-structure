#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Step 2: Routing Views
@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

# Step 3: Variable Routes
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Step 4: Flask Development Web Server
if __name__ == '__main__':
    app.run(port=5555)
