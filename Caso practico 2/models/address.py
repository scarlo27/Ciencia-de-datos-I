import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from models.base_model import BaseModel
from models.city import City

class Address(BaseModel):
    address_id = AutoField()
    address = CharField(max_length=50, constraints=[Check("length(address) > 0")])
    address2 = CharField(max_length=50, null=True)
    district = CharField(max_length=20, null=False)
    city = ForeignKeyField(City, backref='addresses', column_name='city_id')
    postal_code = CharField(max_length=10, null=True)
    phone = CharField(max_length=20, null=False)
    location = BlobField(null=False)  # Campo espacial POINT
    last_update = DateTimeField()

    class Meta:
        table_name = 'address'