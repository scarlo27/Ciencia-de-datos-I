import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controllers.film_controller import FilmController

class FilmView:

    @staticmethod
    def list_all():
        films = FilmController.get_all_films()
        for f in films:
            print(f"{f.film_id} - {f.title} ({f.release_year})")

    @staticmethod
    def search_by_title():
        title = input("Buscar título: ")
        results = FilmController.search_by_title(title)
        for f in results:
            print(f"{f.film_id} - {f.title}")

    @staticmethod
    def search_by_category():
        category = input("Categoría: ")
        results = FilmController.search_by_category(category)
        for f in results:
            print(f"{f.film_id} - {f.title}")
    @staticmethod
    def update_film():
        film_id = int(input("ID de la película a actualizar: "))
        title = input("Nuevo título: ")
        description = input("Descripción: ")
        release_year = int(input("Año de estreno: "))
        rental_duration = int(input("Duración de alquiler (días): "))
        rental_rate = float(input("Tarifa de alquiler: "))

        data = {
            "title": title,
            "description": description,
            "release_year": release_year,
            "rental_duration": rental_duration,
            "rental_rate": rental_rate,
        }

        updated = FilmController.update_film(film_id, data)
        if updated:
            print("Película actualizada con éxito.")
        else:
            print("No se pudo actualizar la película.")

    @staticmethod
    def delete_film():
        film_id = int(input("ID de la película a eliminar: "))
        confirm = input(f"¿Seguro que deseas eliminar la película con ID {film_id}? (s/n): ")
        if confirm.lower() == "s":
            deleted = FilmController.delete_film(film_id)
            if deleted:
                print("Película eliminada con éxito.")
            else:
                print("No se pudo eliminar la película.")
