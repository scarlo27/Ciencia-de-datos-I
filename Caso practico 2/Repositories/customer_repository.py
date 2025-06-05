
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.customer import Customer

class CustomerRepository:

    @staticmethod
    def get_all():
        return list(Customer.select())

    @staticmethod
    def get_by_id(customer_id: int):
        try:
            return Customer.get(Customer.customer_id == customer_id)
        except Customer.DoesNotExist:
            return None

    @staticmethod
    def create(data: dict):
        return Customer.create(**data)

    @staticmethod
    def update(customer_id: int, data: dict):
        return Customer.update(**data).where(Customer.customer_id == customer_id).execute()

    @staticmethod
    def delete(customer_id: int):
        return Customer.delete().where(Customer.customer_id == customer_id).execute()

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        return list(Customer.select().where(
            (Customer.first_name.contains(first_name)) &
            (Customer.last_name.contains(last_name))
        ))

    @staticmethod
    def get_by_store(store_id: int):
        return list(Customer.select().where(Customer.store == store_id))
