
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.actor import Actor

class ActorRepository:

    @staticmethod
    def get_all():
        return list(Actor.select())

    @staticmethod
    def get_by_id(actor_id: int):
        try:
            return Actor.get(Actor.actor_id == actor_id)
        except Actor.DoesNotExist:
            return None

    @staticmethod
    def create(data: dict):
        return Actor.create(**data)

    @staticmethod
    def update(actor_id: int, data: dict):
        return Actor.update(**data).where(Actor.actor_id == actor_id).execute()

    @staticmethod
    def delete(actor_id: int):
        return Actor.delete().where(Actor.actor_id == actor_id).execute()

    @staticmethod
    def search_by_name_or_surname(name: str):
        return list(
            Actor.select().where(
                (Actor.first_name.contains(name)) | (Actor.last_name.contains(name))
            )
        )
