from django.shortcuts import render
import pprint
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TodoModel
from .models import Todo
from datetime import datetime
from .DAO.TodoMongoDBDAO import TodoMongoDBDAO
from .DAO.AbstractTodoDAO import AbstractTodoDao
import dateutil.parser
# Create your views here.
class TodoViews:

    @csrf_exempt
    def index(request):    
        try:
            my_req=request.body.decode('utf-8')
            #myreq_dict = {'username':'abcd'}#newTodo.dueDate=dueDate.now.replace(day=9)
            myreq_dict={}
            myreq_dict.update(json.loads(my_req))
            print(myreq_dict)
            my_response = {'hello':1,'hello2':'ujjvalaluru'}
            sess_array = []
            client = MongoClient('mongodb://127.0.0.1:27017')
            db = client.chatapp
            if "username" in myreq_dict:            
                cursor = db.sessions.find({"username":myreq_dict["username"]})
                for doc in cursor:
                    sess_array.append(doc)
                my_response["sessions"] = sess_array
                
                newTodo = TodoModel()
                newTodo.title="hello"
                newTodo.description="hi"
                newTodo.dueDate=datetime.now()
                newTodo.save()                
                print(TodoModel.objects.filter(title__startswith='h')[0].title)
                #return HttpRespone("Hello World, this is my first Django app")
                return JsonResponse(my_response)
            else:
                my_response["result"]="failure due to user name not being ound"
                return JsonResponse(my_response)
        except ValueError:
            return JsonResponse({'exception':'no json given'})
        
        

    @csrf_exempt
    def insertTodo(request):
        try:
            requestDict = {}
            requestDict.update(json.loads(request.body.decode('utf-8')))
            newTodo = TodoModel()
            todoPojo = Todo()
            if "title" in requestDict:
                newTodo.title=requestDict["title"]
                todoPojo.setTitle(requestDict["title"])                
            if "desc" in requestDict:
                newTodo.description=requestDict["desc"]
                todoPojo.setDescription(requestDict["desc"])
            if "due" in requestDict:
                newTodo.dueDate=dateutil.parser.parse(requestDict["due"])
                todoPojo.setDueDate(dateutil.parser.parse(requestDict["due"]))
            newTodo.save()
            dao = TodoMongoDBDAO()
            dao.saveTodo(todoPojo)
            print(todoPojo.__dict__)
            print("Successfully saved Todo",newTodo.__str__())
            responseDict={'status':"success"}
            responseDict["resp"]="hello"            
            return JsonResponse(responseDict)
        except Exception as e:
            print("exception",e)
            return JsonResponse({'status':"failure due to exception"})

    @csrf_exempt
    def sample_get_request(request):
        try:
            return JsonResponse({'key1':'value1'})
        except Exception as e:
            print("exception", e)
            return JsonResponse({"key1":"exception"})
       
    @csrf_exempt
    def sample_post_request(request):
        print(request.method)
        print("\n\n\n\n\n")
        pp = pprint.PrettyPrinter(indent = 4)
        #pp.pprint(request.META)
        if request.method == "POST":
            #print(request.body.decode('utf-8').strip('\n'))
            #print(str(request.body))
            request_dict = {}
            request_dict.update(json.loads(request.body.decode('utf-8')))
            request_dict["received"] = "yes"
            return JsonResponse(request_dict)
        elif request.method == "OPTIONS":

            return JsonResponse({})


class SomeNewView(View):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        resp={"is":"ujjval"}
        return JsonResponse(resp)
    @csrf_exempt
    def options(self, request, *args, **kwargs):
        resp={}
        return JsonResponse(resp)

        

