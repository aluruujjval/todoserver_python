from .AbstractTodoDAO import AbstractTodoDao
from pymongo import MongoClient
from ..models import Todo
import os
class TodoMongoDBDAO(AbstractTodoDao):
    def __init__(self):
        self.__mongoClient = MongoClient(os.environ["MONGODB_URL"])

    def saveTodo(self, todo):
        db = self.__mongoClient.todoapp
        db.todos.insert_one(todo.__dict__)
    def getTodos(self):
        cursor = self.__mongoClient.todoapp.find()
        for doc in cursor:
            print(doc , "\n\n")

