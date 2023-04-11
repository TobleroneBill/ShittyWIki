from flask import Blueprint, render_template


views = Blueprint('views',__name__)

@views.route('/')
def Game(): # main game
    return render_template("index.html")

@views.route('/leaderboard')
def leaderboard():  # progress and stats against other players
    return render_template("leaderboard.html")

@views.route('/unlocks')
def unlocks(): # User unlocked wiki pages
    return render_template("unlocks.html")