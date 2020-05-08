from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import  User, auth

from .models import UserFavourite
from products.models import Laptop
from orders.models import Order

# Create your views here.
def register(request):

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken') 
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use') 
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, 
                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Your registration was successful and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            if 'next' in request.POST:  # After login redirect to previous page
                return redirect(request.POST.get('next'))   
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')

    return redirect('home')


@login_required # Login required
def add_to_favourite(request, pk):

    laptop = Laptop.objects.get(id=pk)

    already_added = UserFavourite.objects.all().filter(laptop=laptop, user=request.user)
    if already_added:
        messages.error(request, 'This product is already in your favourites list!')
        return redirect('/product/'+str(laptop.id))
        
    favourite = UserFavourite()
    favourite.laptop=laptop
    favourite.user = request.user

    favourite.save()

    messages.success(request, 'Product added to your favourites list!')

    return redirect('/product/'+str(laptop.id))


@login_required # Login required
def remove_from_favourite(request, pk):
    favourite = UserFavourite.objects.get(id=pk)
    favourite.delete()

    return redirect(reverse('dashboard'))


@login_required # Login required
def dashboard(request):

    favourite_list = UserFavourite.objects.all().filter(user=request.user)
    orders =  Order.objects.exclude(status='Started').filter(user=request.user)

    context = {
        'favourite_list':favourite_list,
        'orders': orders,
    }

    return render(request, 'accounts/dashboard.html', context)