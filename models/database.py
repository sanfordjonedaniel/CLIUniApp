import pickle
import os

DATABASE_FILE = "students.data"


class Database:
    @staticmethod
    def _ensure_file():
        if not os.path.exists(DATABASE_FILE):
            with open(DATABASE_FILE, 'wb') as f:
                pickle.dump([], f)

    @staticmethod
    def load():
        Database._ensure_file()
        try:
            with open(DATABASE_FILE, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return []

    @staticmethod
    def save(students):
        with open(DATABASE_FILE, 'wb') as f:
            pickle.dump(students, f)

    @staticmethod
    def clear():
        with open(DATABASE_FILE, 'wb') as f:
            pickle.dump([], f)
