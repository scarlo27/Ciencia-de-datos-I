import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.address import Address
from models.store import Store

class Staff(BaseModel):
    staff_id = AutoField()
    first_name = CharField(max_length=45)
    last_name = CharField(max_length=45)
    address = ForeignKeyField(Address, backref='staff_members', column_name='address_id')
    email = CharField(max_length=50, null=True)
    store = ForeignKeyField(Store, backref='staff_members', column_name='store_id')
    active = BooleanField()
    username = CharField(max_length=16)
    password = CharField(max_length=40, null=True)
    last_update = DateTimeField()

    class Meta:
        table_name = 'staff'