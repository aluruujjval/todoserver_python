from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    dueDate = models.DateTimeField('datedue for todo task',blank=True,null=True)

    def __str__(self):
        #return "{'title':'"+self.title+"','description':'"+self.description+"','dueData':"+self.dueDate+"}"
        return "hello"


class Todo:
    def __init__(self, title, description, dueDate):
        self.__title=title
        self.__description= description
        self.__dueDate=dueDate    
    def __init__(self):
        self.__title = None
        self.__description = None
        self.__dueDate = None
    def getTitle(self):
        return self.__title
    def getDescription(self):
        return self.__description
    def getDueDate(self):
        return self.__dueDate
    def setTitle(self, title):
        self.__title=title
    def setDescription(self, description):
        self.__description= description
    def setDueDate(self, dueDate):
        self.__dueDate=dueDate
        

