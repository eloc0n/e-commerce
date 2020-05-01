from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # seller_email = request.POST['seller_email']

        contact = Contact(product=product, product_id=product_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

        contact.save()

        # Send email
        send_mail(
            'Question about a Product',
            'There has been a question for ' + product + '. Sign into the admin panel for more info',
            'jani.bratja@gmail.com',
            ['johnisb.21@gmail.com'],
            # [seller_email, 'johnisb.21@gmail.com'],
            fail_silently=False
            )

        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('/product/'+product_id)