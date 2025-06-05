import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Repositories.rental_repository import RentalRepository

class RentalController:

    @staticmethod
    def get_all_rentals():
        return RentalRepository.get_all()

    @staticmethod
    def get_rental_by_id(rental_id):
        return RentalRepository.get_by_id(rental_id)

    @staticmethod
    def create_rental(data):
        return RentalRepository.create(data)

    @staticmethod
    def rent_movie(title, first_name, last_name, days):
        return RentalRepository.rent_movie_to_customer(title, first_name, last_name, days)

    @staticmethod
    def update_rental(rental_id, data):
        return RentalRepository.update(rental_id, data)

    @staticmethod
    def delete_rental(rental_id):
        return RentalRepository.delete(rental_id)
