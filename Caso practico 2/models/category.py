import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel

class Category(BaseModel):
    category_id = AutoField()  # PK
    name = CharField(max_length=25, constraints=[Check("length(name) > 0")], unique=True)
    last_update = DateTimeField()

    class Meta:
        table_name = 'category'