from django.urls import path
from .views import *

app_name = 'MarketPlace'

urlpatterns = [
     path('',Home,name="Home"),
     path('card',Card,name="Card")
]
