import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.film import Film
from models.store import Store

class Inventory(BaseModel):
    inventory_id = AutoField()
    film = ForeignKeyField(Film, backref='inventories', column_name='film_id')  # FK
    store = ForeignKeyField(Store,  backref='inventories', column_name='store_id')  # FK
    last_update = DateTimeField()

    class Meta:
        table_name = 'inventory'