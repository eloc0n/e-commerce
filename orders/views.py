import stripe

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.conf import settings

from accounts.forms import UserAddressForm
from accounts.models import UserAddres
from .models import Order
from cart.models import Cart, CartItem
from .utils import id_generator

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret = settings.STRIPE_SECRET_KEY
except Exception as e:
    raise NotImplementedError(str(e))

stripe.api_key = stripe_secret



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
            return redirect(reverse('checkout'))

    context = {
        'address_form':address_form,
    }

    return render(request, 'orders/address.html', context)
    


@login_required # require user login
def checkout(request):
    try:
        the_id = request.session['cart_id'] # if cart id exists grab it
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return redirect(reverse('cart'))
    
    user_address = UserAddres.objects.filter(user=request.user).last() 
   
    try:
        new_order = Order.objects.get(cart=cart, address=user_address)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.address = user_address
        new_order.user = request.user   # assign user to the order
        new_order.order_id = id_generator() 
        new_order.save()
    except:
        new_order = None
        # error message
        return redirect(reverse('cart'))
    
    final_amount = 0
    if new_order is not None: 
        new_order.sub_total = cart.total    # update sub_total when user leaves checkout to add more products
        new_order.save()   
        new_order.get_final_tax_amount()    # final amount
        final_amount = new_order.get_final_amount()  # final amount with taxes included                                                   

    
        

    # run credit card
    if request.method == 'POST':
        try:
            user_stripe = request.user.userstripe.stripe_id
            customer = stripe.Customer.retrieve(user_stripe)
        except:
            customer = None

        if customer is not None:
            token = request.POST['stripeToken']
            card = stripe.Customer.create_source(customer.id, source=token)
            card.address_city = user_address.city
            card.address_line1 = user_address.address
            card.address_line2 = user_address.address2
            card.address_country = user_address.country
            card.address_zip = user_address.zipcode
            card.save()
           
            charge = stripe.Charge.create(
                amount= int(final_amount * 100),
                currency="eur",
                source=card,
                customer=customer.id,
                description="New order from user %s" %(request.user.username),
            )

            if charge['captured']:
                new_order.status = 'Finished'
                new_order.save()
                del request.session['cart_id']
                del request.session['items_total']
                
                messages.success(request, 'Transaction completed successfully. Thank you for you order!')
        
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Something went wrong! We will contact you about details!')

                return redirect(reverse('home'))

    context = {
        'order':new_order,
        'stripe_pub':stripe_pub,
    }

    return render(request, 'orders/checkout.html', context)


@login_required # Login required
def order(request, pk):

    order = Order.objects.get(id=pk)
    cart_id = order.cart_id
    cart = Cart.objects.get(id=cart_id)

    context = {
        'order_invoice' :order,
        'cart':cart,
    }

    return render(request, 'orders/order.html', context)