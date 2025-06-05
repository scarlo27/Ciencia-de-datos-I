from View.customer_view import CustomerView
from View.film_view import FilmView
from View.rental_view import RentalView

def main():
    while True:
        print("\nMenú:")
        print("1. Ver clientes")
        print("2. Buscar películas por categoría")
        print("3. Rentar película")
        print("4. Actualizar película")
        print("5. Eliminar película")
        print("0. Salir")
        opc = input("Opción: ")

        if opc == "1":
            CustomerView.list_all()
        elif opc == "2":
            FilmView.search_by_category()
        elif opc == "3":
            RentalView.rent_movie()
        elif opc == "4":
            FilmView.update_film()
        elif opc == "5":
            FilmView.delete_film()
        elif opc == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()