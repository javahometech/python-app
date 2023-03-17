from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="color:orange">Welcome to Java Home Docker App </h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
