import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.address import Address
from models.store import Store

class Customer(BaseModel):
    customer_id = AutoField()
    store = ForeignKeyField(Store, backref='customers', column_name='store_id')  # FK
    first_name = CharField(max_length=45)
    last_name = CharField(max_length=45)
    email = CharField(max_length=50, null=True)
    address = ForeignKeyField(Address, backref='customers', column_name='address_id')  # FK
    active = BooleanField()
    create_date = DateTimeField()
    last_update = DateTimeField(null=True)

    class Meta:
        table_name = 'customer'