from ..models import TodoModel
from ..models import Todo
from ..DAO.TodoMongoDBDAO import TodoMongoDBDAO

class TodoMgmtService:
    def __init__(self):
        self.__dao  = TodoMongoDBDAO()