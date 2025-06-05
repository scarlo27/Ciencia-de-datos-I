import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.language import Language

class Film(BaseModel):
    film_id = AutoField()  # PK
    title = CharField(max_length=255)
    description = TextField(null=True)
    release_year = IntegerField(null=True)
    language = ForeignKeyField(Language, backref="films", column_name="language_id")  # FK
    original_language = ForeignKeyField(Language, backref="original_films", column_name="original_language_id", null=True)
    rental_duration = IntegerField(constraints=[Check("rental_duration > 0")])
    rental_rate = DecimalField(max_digits=4, decimal_places=2)
    length = IntegerField(null=True)
    replacement_cost = DecimalField(max_digits=5, decimal_places=2)
    rating = CharField(max_length=5, null=True)
    special_features = CharField(max_length=255, null=True)
    last_update = DateTimeField()

    class Meta:
        table_name = 'film'