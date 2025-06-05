import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.actor import Actor
from models.film import Film

class FilmActor(BaseModel):
    actor = ForeignKeyField(Actor, backref='film_actors', column_name='actor_id')
    film = ForeignKeyField(Film, backref='film_actors', column_name='film_id')
    last_update = DateTimeField()

    class Meta:
        table_name = 'film_actor'
        primary_key = CompositeKey('actor', 'film')