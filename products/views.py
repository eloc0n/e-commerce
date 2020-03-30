from django.shortcuts import render

# Create your views here.

def home(request):

    context = {
        
    }

    return render(request, 'products/home.html', context)


def products(request):

    context = {
        
    }

    return render(request, 'products/products.html', context)


def product(request, pk):

    context = {
        
    }

    return render(request, 'product/product.html', context)