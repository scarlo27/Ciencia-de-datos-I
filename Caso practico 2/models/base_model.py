# base_model.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import Model
from dbcontext import db

class BaseModel(Model):
    class Meta:
        database = db