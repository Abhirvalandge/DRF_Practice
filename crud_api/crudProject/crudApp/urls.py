from django.urls import path
from .views import *

urlpatterns = [
    path('list/',EmployeeListApi.as_view()),
    path('create/', EmployeeCreateApi.as_view()),
    path('update/<int:pk>',EmployeeUpdateApi.as_view()),
    path('delete/<int:pk>',EmployeeDeleteApi.as_view()),
]
