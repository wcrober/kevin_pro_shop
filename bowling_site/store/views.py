from django.shortcuts import render
from .models import Category, Product, Service



def products(request):
    all_products = Product.objects.all() # get products from data base
    return render(request, 'store/products.html', {'products': all_products}) # render the html page with the products

def services(request):
    all_services = Service.objects.all()
    return render(request, 'store/services.html', {'service': all_services})

def home(request):
    return render(request, 'store/home.html')

