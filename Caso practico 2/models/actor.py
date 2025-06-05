import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel

class Actor(BaseModel):
    actor_id = AutoField()  # PK
    first_name = CharField(max_length=45, constraints=[Check("length(first_name) > 0")])
    last_name = CharField(max_length=45, constraints=[Check("length(last_name) > 0")])
    last_update = DateTimeField()

    class Meta:
        table_name = 'actor'