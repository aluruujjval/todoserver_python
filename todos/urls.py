from django.urls import path, re_path
from django.conf.urls import url
from .views import TodoViews
from .views import SomeNewView
from .views import MyCrudViews

urlpatterns = [
    path('hellojson/',TodoViews.index, name='index'),
    path('addTodo/',TodoViews.insertTodo, name='addtodo'),
    path('sampleget/',TodoViews.sample_get_request, name='someget'),
    path('samplepost/',TodoViews.sample_post_request, name= "somepost"),
    path('insertTodo/', MyCrudViews.saveNewTODO , name= "newTODO"),
    #path('getTodos/title-P<title>/',MyCrudViews.getTODOS, name = "getTODOS"),
    #re_path(r'^getTodos/(?:title-(?P<title>\w+)/)?$', MyCrudViews.getTODOS, name = "getTODOS"), 
    re_path(r'^getTodos/title-(?P<title>\w+)$', MyCrudViews.getTODOS, name = "getTODOS"), 
    url("samplepost2/",SomeNewView.as_view(), name="someposr2"),
]

