import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.customer import Customer
from models.staff import Staff
from models.rental import Rental

class Payment(BaseModel):
    payment_id = AutoField()
    customer = ForeignKeyField(Customer, backref='payments', column_name='customer_id')
    staff = ForeignKeyField(Staff, backref='payments', column_name='staff_id')
    rental = ForeignKeyField(Rental, backref='payments', column_name='rental_id', null=True)
    amount = DecimalField(max_digits=5, decimal_places=2)
    payment_date = DateTimeField()

    class Meta:
        table_name = 'payment'