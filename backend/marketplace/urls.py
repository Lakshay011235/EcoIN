from django.urls import path
from .views import *

app_name = 'MarketPlace'

urlpatterns = [
     path('',Home,name="Home"),
     path('cart',ProductsCart,name="Cart"),
     path('wishlist',ProductsWishlist,name="Wishlist")
]
