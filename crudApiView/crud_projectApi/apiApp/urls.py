from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('listApiView/', TodoListApiView.as_view()),
    path('detail_api/<int:todo_id>/', TodoDetailApiView.as_view()),
]