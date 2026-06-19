import click
from flask import Flask
from flask import current_app, g

from . import PokemonDatabase

#region GENERIC FLASK DB THINGS 
#https://flask.palletsprojects.com/en/stable/tutorial/database/
def _get_db(dbName:str):
    if dbName not in g:
        g.setdefault(dbName, PokemonDatabase(current_app))

    return g.get(dbName)

def init_db(dbName:str):
    db = _get_db(dbName)

#endregion

#region POKEMON DB STUFF
POKEMON_DB_NAME = "poke-bd"

@click.command('init-poke-db')
def init_poke_db_command():
    """Create new Pokemon DB file instance """

    init_db(POKEMON_DB_NAME)
    click.echo('Initialized the database.')

def get_pokemon_db() -> PokemonDatabase:
    return _get_db(POKEMON_DB_NAME)

def close_poke_db(e=None):
    g.pop(POKEMON_DB_NAME, None)

def init_app(app: Flask):
    app.teardown_appcontext(close_poke_db) # type: ignore
    app.cli.add_command(init_poke_db_command)

#endregion
