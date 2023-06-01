from django.urls import path
from .views import *

app_name = 'Base'

urlpatterns = [
    path('',Home,name="Home"),
    path('login',Login,name="Login"),
    path('logout',Logout,name="Logout")
]