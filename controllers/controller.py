
from flask import render_template
from app import app
from models.player import Player
from models.game import Game


@app.route('/')
def home():
    return 'Home'