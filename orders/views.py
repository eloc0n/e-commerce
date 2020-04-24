from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from accounts.forms import UserAddressForm
from accounts.models import UserAddres
# from .models import Order
# from shopping_cart.models import Cart
# from .utils import id_generator


# Create your views here.
@login_required # require user login
def address(request):
    # assign an address 
    address_form = UserAddressForm(request.POST or None) 
    if request.method == 'POST':
        # try:
        #     user_address = UserAddres.objects.get(user=request.user)
        #     user_address.delete()
        # except:
        #     user_address = None

        if address_form.is_valid:
            new_address = address_form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            return redirect(reverse('checkout'))

    context = {
        'address_form':address_form,
    }

    return render(request, 'orders/address.html', context)
    