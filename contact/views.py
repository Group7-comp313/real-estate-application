from django.shortcuts import render,redirect
from .models import Contact
def contact(request):
    if request.method == "POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        #contact_date = request.POST['contact_date']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact= Contact(listing=listing,listing_id=listing_id,name=name,
                       email=email,phone=phone,message=message,user_id=user_id,realtor_email=realtor_email
                       )
        contact.save()

        return redirect('/listings/'+listing_id)





# Create your views here.
