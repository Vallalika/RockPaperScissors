from flask import render_template
from app import app
from models.player import Player
from models.game import Game
from models.play_game import *

@app.route('/')
def home():
    return 'Home'

@app.route('/<choice1>/<choice2>')
def game_result(choice1, choice2):
    return render_template("index.html", title = "Game results", game_results = results, choice = choice1)