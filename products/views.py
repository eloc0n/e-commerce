from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .choices import screen_choices, price_choices, ram_choices, cores_choices, manufacturer_choices
from .models import Laptop
# Create your views here.

def home(request):

    products = Laptop.objects.all().filter(bestseller=True)[:3]

    context = {
        'products':products,
        'screen_choices':screen_choices,
        'price_choices':price_choices,
        'ram_choices':ram_choices,
        'cores_choices':cores_choices,
        'manufacturer_choices':manufacturer_choices,
    }

    return render(request, 'products/home.html', context)



def products(request):

    products = Laptop.objects.all()

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    
    context = {
        'products':paged_products,
    }

    return render(request, 'products/products.html', context)



def product(request, pk):

    laptop = Laptop.objects.get(id=pk)

    context = {
        'laptop':laptop
    }

    return render(request, 'products/product.html', context)



def search(request):

    queryset_list = Laptop.objects.order_by('-price')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Screen
    if 'screen_resolution' in request.GET:
        screen_resolution = request.GET['screen_resolution']
        if screen_resolution:
            queryset_list = queryset_list.filter(screen_resolution__iexact=screen_resolution)

    # Cores
    if 'cores' in request.GET:
        cores = request.GET['cores']
        if cores:
            queryset_list = queryset_list.filter(cores__iexact=cores)

    # Manufacturer
    if 'manufacturer' in request.GET:
        manufacturer = request.GET['manufacturer']
        if manufacturer:
            queryset_list = queryset_list.filter(manufacturer__iexact=manufacturer)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Ram
    if 'ram' in request.GET:
        ram = request.GET['ram']
        if ram:
            queryset_list = queryset_list.filter(ram__iexact=ram)


    context = {
        'products':queryset_list,
        'screen_choices':screen_choices,
        'price_choices':price_choices,
        'ram_choices':ram_choices,
        'cores_choices':cores_choices,
        'manufacturer_choices':manufacturer_choices,
        'values':request.GET,
    }


    return render(request, 'products/search.html', context)