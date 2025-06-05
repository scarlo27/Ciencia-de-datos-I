import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.film import Film
from models.category import Category

class FilmCategory(BaseModel):
    film = ForeignKeyField(Film, backref='film_categories', column_name='film_id')
    category = ForeignKeyField(Category, backref='film_categories', column_name='category_id')
    last_update = DateTimeField()

    class Meta:
        table_name = 'film_category'
        primary_key = CompositeKey('film', 'category')