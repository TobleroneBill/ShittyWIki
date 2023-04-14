from flask import Flask, url_for
import os, pathlib, sys, json


def Create_App():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lol'

    from .views import views

    app.register_blueprint(views,urlprefix='/')
    return app

