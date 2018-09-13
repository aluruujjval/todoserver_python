from django.urls import path
from django.conf.urls import url
from .views import TodoViews
from .views import SomeNewView

urlpatterns = [
    path('hellojson/',TodoViews.index, name='index'),
    path('addTodo/',TodoViews.insertTodo, name='addtodo'),
    path('sampleget/',TodoViews.sample_get_request, name='someget'),
    path('samplepost/',TodoViews.sample_post_request, name= "somepost"),
    url("samplepost2/",SomeNewView.as_view(), name="someposr2"),
]

