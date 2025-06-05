import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel

class Country(BaseModel):
    country_id = AutoField()  # PK
    country = CharField(max_length=50, constraints=[Check("length(country) > 0")], unique=True)
    last_update = DateTimeField()

    class Meta:
        table_name = 'country'