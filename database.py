from pymongo import MongoClient
from pymongo.database import Database


def get_database() -> Database:
    client = MongoClient("mongodb://localhost:27017/")
    return client["task_manager"]


from typing import List, Dict, Any
from database import get_database
from pymongo.collection import Collection


def add_task(task: Dict[str, Any]) -> str:
    db = get_database()
    collection = db["tasks"]
    result = collection.insert_one(task)
    return str(result.inserted_id)


def view_all_tasks() -> List[Dict[str, Any]]:
    db = get_database()
    collection = db["tasks"]
    return list(collection.find())


def update_task_status(task_id: str, status: str) -> int:
    db = get_database()
    collection = db["tasks"]
    result = collection.update_one({"_id": task_id}, {"$set": {"status": status}})
    return result.modified_count


def delete_task(task_id: str) -> int:
    db = get_database()
    collection = db["tasks"]
    result = collection.delete_one({"_id": task_id})
    return result.deleted_count


import re


class User:
    def __init__(self, password: str):
        self._password = password

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if not self.is_password_strong(value):
            raise ValueError("Password is not strong enough")
        self._password = value

    @staticmethod
    def is_password_strong(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        return True
