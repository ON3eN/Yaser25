from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})
