from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from accounts.forms import UserAddressForm
from accounts.models import UserAddres
# from .models import Order
# from cart.models import Cart
# from .utils import id_generator


# Create your views here.
@login_required # require user login
def address(request):
    try:
        user_address = UserAddres.objects.filter(user=request.user).last() # grab stored address
        initial = {
                    'address': user_address.address,
                    'address2': user_address.address2,
                    'city': user_address.city,
                    'country': user_address.country,
                    'zipcode': user_address.zipcode,
                    'phone': user_address.phone
        }
        
        address_form = UserAddressForm(request.POST or initial) # display stored address

    except:
        address_form = UserAddressForm(request.POST or None) # assign new address
        
    if request.method == 'POST':
        # try:
        #     user_address = UserAddres.objects.filter(user=request.user).first()
        #     user_address.delete()
        # except:
        #     user_address = None

        if address_form.is_valid:
            new_address = address_form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            return redirect(reverse('home'))

    context = {
        'address_form':address_form,
    }

    return render(request, 'orders/address.html', context)
    