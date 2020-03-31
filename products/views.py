from django.shortcuts import render

from .models import Laptop
# Create your views here.

def home(request):

    products = Laptop.objects.all().filter(bestseller=True)[:3]

    context = {
        'products':products,
    }

    return render(request, 'products/home.html', context)


def products(request):

    products = Laptop.objects.all()
    
    context = {
        'products':products,
    }

    return render(request, 'products/products.html', context)


def product(request, pk):

    laptop = Laptop.objects.get(id=pk)

    context = {
        'laptop':laptop
    }

    return render(request, 'products/product.html', context)