import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Repositories.film_repository import FilmRepository

class FilmController:

    @staticmethod
    def get_all_films():
        return FilmRepository.get_all()

    @staticmethod
    def get_film_by_id(film_id):
        return FilmRepository.get_by_id(film_id)

    @staticmethod
    def search_by_title(title):
        return FilmRepository.get_by_title(title)

    @staticmethod
    def search_by_category(category_name):
        return FilmRepository.get_by_category_name(category_name)

    @staticmethod
    def create_film(data):
        return FilmRepository.create(data)

    @staticmethod
    def update_film(film_id, data):
        return FilmRepository.update(film_id, data)

    @staticmethod
    def delete_film(film_id):
        return FilmRepository.delete(film_id)
