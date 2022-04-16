from flask import render_template, request
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

@app.route('/index', methods=['POST'])
def game_result():
    player_name = request.form["player_name"]
    player_choice = request.form["player_choice"]
    print(request.form)
    game = Game()
    human_player = Player(player_name, player_choice)
    results = game.play_with_computer(human_player)
    computer_choice = game.get_computer_choice()
    print("Computer choice: ", computer_choice)
    return render_template("index.html", title = "Rock-Paper-Scissors", game_results = results, choice = player_choice, name = player_name)