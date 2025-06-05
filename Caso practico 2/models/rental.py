import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.inventory import Inventory
from models.customer import Customer
from models.staff import Staff

class Rental(BaseModel):
    rental_id = AutoField()
    rental_date = DateTimeField()
    inventory = ForeignKeyField(Inventory, backref='rentals', column_name='inventory_id')
    customer = ForeignKeyField(Customer, backref='rentals', column_name='customer_id')
    return_date = DateTimeField(null=True)
    staff = ForeignKeyField(Staff, backref='rentals', column_name='staff_id')
    last_update = DateTimeField()

    class Meta:
        table_name = 'rental'