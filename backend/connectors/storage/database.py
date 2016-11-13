from django.core.cache import caches

from config import database


class DatabaseConnector:
    db = []

    def __init__(self):
        self.db = caches[database.DB_BACKEND]

    def set_user(self, user):
        return self.db.set(database.PRE_USER + str(user.id), user)

    def get_user(self, user_id):
        return self.db.get(database.PRE_USER + str(user_id))
