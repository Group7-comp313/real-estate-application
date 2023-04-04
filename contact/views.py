from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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

        #check if user has made inquary already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id =listing_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry for thi listing')
                return redirect('/listings/'+listing_id)

        contact= Contact(listing=listing,listing_id=listing_id,name=name,
                       email=email,phone=phone,message=message,user_id=user_id,realtor_email=realtor_email
                       )
        contact.save()
        # send Email
        send_mail(
            #auth_user=settings.EMAIL_HOST_USER,
            #auth_password=settings.EMAIL_HOST_PASSWORD,
            subject='propery listing Inquary',
            message='There has been a inquiry for '+listing+'.sign into admin panel for more info',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[realtor_email,'group7.comp313@gmail.com',email]
        )
        messages.success(request, 'requeste has been submitted, realtor will get back to you yo soon')

        return redirect('/listings/'+listing_id)





# Create your views here.
