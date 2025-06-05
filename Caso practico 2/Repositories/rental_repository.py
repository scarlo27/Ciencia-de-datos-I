
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import fn
from models.rental import Rental
from models.film import Film
from models.inventory import Inventory
from models.customer import Customer
from models.staff import Staff
from datetime import datetime, timedelta

class RentalRepository:

    @staticmethod
    def get_all():
        return list(Rental.select())

    @staticmethod
    def get_by_id(rental_id: int):
        try:
            return Rental.get(Rental.rental_id == rental_id)
        except Rental.DoesNotExist:
            return None

    @staticmethod
    def create(data: dict):
        return Rental.create(**data)

    @staticmethod
    def update(rental_id: int, data: dict):
        return Rental.update(**data).where(Rental.rental_id == rental_id).execute()

    @staticmethod
    def delete(rental_id: int):
        return Rental.delete().where(Rental.rental_id == rental_id).execute()

    @staticmethod
    def rent_movie_to_customer(title: str, first_name: str, last_name: str, days: int):
        try:
            # Buscar cliente
            customer = Customer.get(
                (Customer.first_name == first_name) & (Customer.last_name == last_name)
            )

            # Buscar película
            film = Film.get(Film.title == title)

            # Buscar inventario disponible
            inventory_item = (
                Inventory.select()
                .where(Inventory.film == film.film_id)
                .order_by(fn.Rand()) 
                .first()
            )

            if not inventory_item:
                raise Exception("No hay copias disponibles de la película.")

            # Staff por defecto (usamos el primero en la base)
            staff = Staff.select().first()

            # Crear registro de alquiler
            rental = Rental.create(
                rental_date=datetime.now(),
                inventory=inventory_item,
                customer=customer,
                return_date=datetime.now() + timedelta(days=days),
                staff=staff,
                last_update=datetime.now()
            )

            return rental

        except Customer.DoesNotExist:
            raise Exception("Cliente no encontrado.")
        except Film.DoesNotExist:
            raise Exception("Película no encontrada.")
