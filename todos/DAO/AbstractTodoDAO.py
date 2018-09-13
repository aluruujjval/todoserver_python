from abc import ABC, abstractmethod
from ..models import Todo
class AbstractTodoDao(ABC):
    @abstractmethod
    def saveTodo(self,todo):
        pass
    @abstractmethod
    def getTodos(self):
        pass
    # @abstractmethod
    # def getTodosByDate(self):
    #     pass