
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.film import Film
from models.film_category import FilmCategory
from models.category import Category

class FilmRepository:

    @staticmethod
    def get_all():
        return list(Film.select())

    @staticmethod
    def get_by_id(film_id: int):
        try:
            return Film.get(Film.film_id == film_id)
        except Film.DoesNotExist:
            return None

    @staticmethod
    def create(data: dict):
        return Film.create(**data)

    @staticmethod
    def update(film_id: int, data: dict):
        return Film.update(**data).where(Film.film_id == film_id).execute()

    @staticmethod
    def delete(film_id: int):
        return Film.delete().where(Film.film_id == film_id).execute()

    @staticmethod
    def get_by_title(title: str):
        return list(Film.select().where(Film.title.contains(title)))

    @staticmethod
    def get_by_category_name(category_name: str):
        return list(
            Film.select()
                .join(FilmCategory)
                .join(Category)
                .where(Category.name.contains(category_name))
        )
