import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.address import Address
# from models.staff import Staff

class Store(BaseModel):
    store_id = AutoField()
    manager_staff_id = IntegerField()  # FK a staff (declarado después)
    address = ForeignKeyField(Address, backref='stores', column_name='address_id')
    last_update = DateTimeField()

    class Meta:
        table_name = 'store'