from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        realtor_email = request.POST['realtor_email']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, 
        message=message, user_id=user_id )

        #Save to ddb
        contact.save()

        messages.success(request, 'Your request has been submitted friend, a realtor will contact you soon')
        return redirect('/listings/'+listing_id)