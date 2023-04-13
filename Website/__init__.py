from flask import Flask

def getPic():
    print('This gets a pic :)')

def Create_App():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lol'

    from .views import views

    app.register_blueprint(views,urlprefix='/')
    app.jinja_env.globals.update(getPic=getPic)     # This means it can be called using flask jinja2
    print('hi')
    return app

