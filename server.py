from flask import Flask
#from python_api.src.Pokemon import 
app = Flask(__name__)

## HOME
@app.route('/')
def hello_world():
   return 'Hello World'

## POKEMON
@app.route('/pokemon')
def pokemon():
   return 'Hello World'

## MUSIC
@app.route('/music')
def music():
   return 'Hello World'

## UGH
@app.route('/ugh')
def ugh():
   return 'Hello World'


@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


if __name__ == '__main__':
   app.run(port=8000, debug=True)