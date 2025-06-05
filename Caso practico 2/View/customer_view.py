import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controllers.customer_controller import CustomerController

class CustomerView:

    @staticmethod
    def list_all():
        customers = CustomerController.get_all_customers()
        for c in customers:
            print(f"{c.customer_id} - {c.first_name} {c.last_name} (Store {c.store.store_id})")

    @staticmethod
    def search_by_name():
        first = input("Nombre del cliente: ")
        last = input("Apellido del cliente: ")
        results = CustomerController.search_customers_by_name(first, last)
        for c in results:
            print(f"{c.customer_id} - {c.first_name} {c.last_name}")

    @staticmethod
    def add_customer():
        data = {
            "store": int(input("ID de tienda: ")),
            "first_name": input("Nombre: "),
            "last_name": input("Apellido: "),
            "email": input("Email: "),
            "address": int(input("ID de dirección: ")),
            "active": True,
            "create_date": input("Fecha de creación (YYYY-MM-DD): "),
            "last_update": input("Última actualización (YYYY-MM-DD HH:MM:SS): ")
        }
        nuevo = CustomerController.create_customer(data)
        print(f"Cliente creado: {nuevo.customer_id}")
