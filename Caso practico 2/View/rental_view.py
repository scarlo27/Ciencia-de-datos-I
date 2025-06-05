import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controllers.rental_controller import RentalController

class RentalView:

    @staticmethod
    def list_all():
        rentals = RentalController.get_all_rentals()
        for r in rentals:
            print(f"{r.rental_id} - Película ID {r.inventory.film.film_id} para {r.customer.first_name} {r.customer.last_name}")

    @staticmethod
    def rent_movie():
        title = input("Título de la película: ")
        first_name = input("Nombre del cliente: ")
        last_name = input("Apellido del cliente: ")
        days = int(input("Días de alquiler: "))

        try:
            rental = RentalController.rent_movie(title, first_name, last_name, days)
            print(f"Renta creada con ID: {rental.rental_id}")
        except Exception as e:
            print("Error al rentar:", str(e))
