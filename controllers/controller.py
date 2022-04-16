
from flask import render_template
from app import app
from models.player import Player
from models.game import Game
from models.play_game import *



@app.route('/')
def home():
    return 'Home'

# @app.route('/<choice1>/<choice2>')
# def game_result(choice1, choice2):
#     game.play_game(player1,player2)