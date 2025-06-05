import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Repositories.customer_repository import CustomerRepository

class CustomerController:

    @staticmethod
    def get_all_customers():
        return CustomerRepository.get_all()

    @staticmethod
    def get_customer_by_id(customer_id):
        return CustomerRepository.get_by_id(customer_id)

    @staticmethod
    def search_customers_by_name(first_name, last_name):
        return CustomerRepository.get_by_name(first_name, last_name)

    @staticmethod
    def get_customers_by_store(store_id):
        return CustomerRepository.get_by_store(store_id)

    @staticmethod
    def create_customer(data):
        return CustomerRepository.create(data)

    @staticmethod
    def update_customer(customer_id, data):
        return CustomerRepository.update(customer_id, data)

    @staticmethod
    def delete_customer(customer_id):
        return CustomerRepository.delete(customer_id)
