from flask import Blueprint, render_template
import pathlib,os,sys,random,json

views = Blueprint('views',__name__)

# Returns a single random image. Paths seem to start from 1 above main.py
def randImg():
    imagePath = pathlib.Path().parent / 'Website' / 'static' / 'images'
    imageList = os.listdir(imagePath)
    image = imageList[random.randint(0,len(imageList)-1)]
    finalPath = pathlib.Path() / 'static' / 'images' / image
    return (str(finalPath),str(image).split('.jpg'))

def getNames(img):
    names = []
    with open(pathlib.Path().cwd() / 'Website' / 'static' / 'ImgData.json','r') as jsonData:
        data = json.load(jsonData)
        keys = list(data.keys())
    
    for i in range(0,7):
        index = random.randint(0,len(keys)-1)
        if keys[index] == img:  # get another key if its the same as the original one to avoid duplicates
            index = random.randint(0,len(keys)-1)

        names.append(keys[index])
    names.append(img)
    random.shuffle(names)   # Shuffles to randomize positions
    return names
    

@views.route('/')
def Game(): # main game
    mainimg = randImg()
    names = getNames(mainimg[1][0])
    return render_template("index.html",img=mainimg,names=names)

@views.route('/leaderboard')
def leaderboard():  # progress and stats against other players
    return render_template("leaderboard.html")

@views.route('/unlocks')
def unlocks(): # User unlocked wiki pages
    return render_template("unlocks.html")