from flask import (
    Blueprint, render_template, request#current_app, flash, g, redirect,  session, url_for
)
from api.file_database import get_pokemon_db
from api.models.Pokemon import buildCardModel

homeBP = Blueprint('home', __name__, url_prefix='/home')

@homeBP.route('/', methods=['GET'])
def home():
    p_db = get_pokemon_db()
    data = p_db.getRandomPokemonByType("Water")
    if data.count != 0:
         cardModel = buildCardModel(data.results[0])
         return render_template('home/readFile.html', locals=cardModel)
    else:
        return render_template('/error.html')
    
    

@homeBP.route('/read-file-test', methods=['GET'])
def readFile():
    if request.method == 'GET':
        return render_template('home/readFile.html')
    
    return render_template('/error.html')
    #return redirect(url_for("auth.login"))
    