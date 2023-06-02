from django.urls import path
from .views import *

app_name = "Carbon"

urlpatterns = [
    path('',Home,name="Home")
]
