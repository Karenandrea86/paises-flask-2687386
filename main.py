from flask import Flask

""" comentario"""
app = Flask(__name__)


@app.route("/")
def index():
    return "hola 2687386"