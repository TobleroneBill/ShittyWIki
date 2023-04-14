from flask import Blueprint, render_template
import pathlib,os,sys,random

views = Blueprint('views',__name__)

def randImg():
    imagePath = pathlib.Path().parent / 'Website' / 'static' / 'images'
    print(imagePath,file=sys.stderr)
    imageList = os.listdir(imagePath)
    finalPath = pathlib.Path() / 'static' / 'images' / imageList[random.randint(0,len(imageList)-1)]
    print(finalPath,file=sys.stderr)
    return str(finalPath)


@views.route('/')
def Game(): # main game
    return render_template("index.html",img=randImg())

@views.route('/leaderboard')
def leaderboard():  # progress and stats against other players
    return render_template("leaderboard.html")

@views.route('/unlocks')
def unlocks(): # User unlocked wiki pages
    return render_template("unlocks.html")