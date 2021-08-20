from django.urls import path
from .views import *

urlpatterns = [
    path('get-inventory/',GetServerDetails.as_view()),
    path('get-inventory2/',GetServerDetailsApi2.as_view()),
    
]