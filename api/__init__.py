from flask import Flask
from . import file_database
from .home import homeBP
import os 

def create_app():
   app = Flask(__name__)

   # ensure the instance folder exists
   os.makedirs(app.instance_path, exist_ok=True)
   
   file_database.init_app(app)
   ## Home
   app.register_blueprint(homeBP)
   
   return app
   ##


   # ## HOME
   # @app.route('/')
   # def hello_world():
   #    return 'Hello World'

   # ## POKEMON
   # @app.route('/pokemon')
   # def pokemon():
   #    return 'Hello World'

   # ## MUSIC
   # @app.route('/music')
   # def music():
   #    return 'Hello World'

   # ## UGH
   # @app.route('/ugh')
   # def ugh():
   #    return 'Hello World'


   # @app.route('/hello/<name>')
   # def hello_name(name):
   #    return 'Hello %s!' % name
   
   
