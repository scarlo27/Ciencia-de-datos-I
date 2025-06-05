import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Repositories.actor_repository import ActorRepository

class ActorController:

    @staticmethod
    def get_all_actors():
        return ActorRepository.get_all()

    @staticmethod
    def get_actor_by_id(actor_id):
        return ActorRepository.get_by_id(actor_id)

    @staticmethod
    def search_by_name(name):
        return ActorRepository.search_by_name_or_surname(name)

    @staticmethod
    def create_actor(data):
        return ActorRepository.create(data)

    @staticmethod
    def update_actor(actor_id, data):
        return ActorRepository.update(actor_id, data)

    @staticmethod
    def delete_actor(actor_id):
        return ActorRepository.delete(actor_id)
