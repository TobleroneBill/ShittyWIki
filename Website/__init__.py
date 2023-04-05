from flask import Flask

def Create_App():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lol'

    from .views import views

    app.register_blueprint(views,urlprefix='/')
    print('hi')
    return app