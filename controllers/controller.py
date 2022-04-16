from flask import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route('/')
def home():
    return "Home"

@app.route('/welcome')
def welcome():
    return render_template("welcome.html", title = "Rock-Paper-Scissors")

@app.route('/play')
def play():
    return render_template("play.html", title = "Rock-Paper-Scissors")

@app.route('/<choice1>/<choice2>')
def index(choice1, choice2):
    player1 = Player(choice1)
    player2 = Player(choice2)
    game = Game()
    results = game.play_game(player1,player2)
    return render_template("index.html", title = "Rock-Paper-Scissors", game_results = results, choice = choice1)