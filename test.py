from typing import List, Dict, Any
from database import get_database
from pymongo.collection import Collection
from pymongo import MongoClient
from pymongo.database import Database


# def add_task(task: Dict[str, Any]) -> str:
#     client = MongoClient("mongodb://localhost:27017/")
#     db = client["task_manager"]
#     collection = db["tasks"]
#     result = collection.insert_one(task)
#     return str(result.inserted_id)


# def view_all_tasks() -> List[Dict[str, Any]]:
#     db = get_database()
#     collection = db["tasks"]
#     return list(collection.find())


# def update_task_status(task_id: str, status: str) -> int:
#     db = get_database()
#     collection = db["tasks"]
#     result = collection.update_one({"_id": task_id}, {"$set": {"status": status}})
#     return result.modified_count


def delete_task(task_id: str) -> int:
    # db = get_database()
    client = MongoClient("mongodb://localhost:27017/")
    db = client["task_manager"]
    collection = db["tasks"]
    result = collection.delete_one({"id": task_id})
    return result.deleted_count


delete_task("646a24ef2d20d64c5b31df47")
