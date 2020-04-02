from django.shortcuts import render, redirect, reverse

from .models import Cart, CartItem
from products.models import Laptop

# Create your views here.

def cart(request):

    try:
        the_id = request.session['cart_id']  # if cart id exist grab it
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None


    if the_id:
        new_total = 0.00
        nav_total = 0
        for item in cart.cartitem_set.all(): # cartitem_set looks for the foreign key relation in CartItem
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            nav_total += item.quantity
        
        
        request.session['items_total'] = nav_total  # get the total amount of items in cart and we will use this 
                                                    # to display next to cart navbar the total amount in cart
       
        # request.session['items_total'] = cart.cartitem_set.count()
       
        cart.total = new_total
        cart.save()

        context = {
            'cart': cart,
        }

    else:
        empty_message = "Your cart is empty!"
        context = {
            'empty':True,
            'empty_message':empty_message,
        }


    return render(request, 'cart/cart.html', context)



def add_to_cart(request, pk):

    request.session.set_expiry(3600)
    
    try:
        the_id = request.session['cart_id']
    except:
        new_cart  = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Laptop.objects.get(id=pk)
    except Laptop.DoesNotExist:
        pass
    except:
        pass

    if request.method == 'POST':
        qty = request.POST['qty']
        print(qty)
        if int(qty) >= 1:
            print('hi')
            cart_item = CartItem.objects.create(cart=cart, product=product)
            print(cart_item)

            cart_item.quantity = qty
            cart_item.save()
        
            return redirect(reverse('cart'))


    return redirect(reverse('cart'))