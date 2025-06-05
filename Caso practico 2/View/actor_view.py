import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controllers.actor_controller import ActorController

class ActorView:

    @staticmethod
    def list_all():
        actors = ActorController.get_all_actors()
        for a in actors:
            print(f"{a.actor_id} - {a.first_name} {a.last_name}")

    @staticmethod
    def search():
        name = input("Buscar nombre o apellido: ")
        results = ActorController.search_by_name(name)
        for a in results:
            print(f"{a.actor_id} - {a.first_name} {a.last_name}")
