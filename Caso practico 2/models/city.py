import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.country import Country

class City(BaseModel):
    city_id = AutoField()  # PK
    city = CharField(max_length=50, constraints=[Check("length(city) > 0")], unique=True)
    country = ForeignKeyField(Country, backref='cities', column_name='country_id')  # FK a Country
    last_update = DateTimeField()

    class Meta:
        table_name = 'city'