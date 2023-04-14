from flask import Blueprint, render_template
import pathlib,os,sys,random,json

views = Blueprint('views',__name__)

def randImg():
    imagePath = pathlib.Path().parent / 'Website' / 'static' / 'images'
    imageList = os.listdir(imagePath)
    image = imageList[random.randint(0,len(imageList)-1)]
    finalPath = pathlib.Path() / 'static' / 'images' / image
    return (str(finalPath),str(image).split('.jpg'))

def getNames(img):
    names = []
    with open(r'Website\static\ImgData.json','r') as jsonData:
        data = json.load(jsonData)
        keys = list(data.keys())
    
    for i in range(0,7):
        index = random.randint(0,len(keys)-1)

        if keys[index] == img:
            index = random.randint(0,len(keys)-1)
            
        names.append(keys[index])
    names.append(img)

    print(names,file=sys.stderr)

    random.shuffle(names)

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