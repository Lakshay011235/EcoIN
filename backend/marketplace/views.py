from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict

# Create your views here.
def Home(request):
    products_obj = Product.objects.all()
    products = []
    for i in products_obj:
        products.append(model_to_dict(i))

    context = { "items" : products }
    return render(request,'marketplace/productcard.html',context=context)

def ProductsCart(request):
    return render(request,'marketplace/productcard.html')

def ProductsWishlist(request):
    return render(request,'marketplace/productcard.html')

def ProductPage(request,id):
    products_obj = Product.objects.filter(id = id).first()
    product = model_to_dict(products_obj)
    context = product
    print(context)
    return render(request,"marketplace/SingleCard.html",context=context)