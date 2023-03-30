from django.shortcuts import render,redirect
#from .forms import CustomUserCreatedForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from contact.models import Contact
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def register(request):
    #form = CustomUserCreatedForm()
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"hello Choose Other Username")

            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.success(request, "profile created ")
                return redirect('signin')
        else:
            messages.success(request,"you have registered ")

    return render(request,'accounts/register.html')

def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        person = authenticate(request,username=username,password=password)
        if person is not None:
            login(request,person)
            messages.success(request,"login sucess")
            return redirect('dashboard')
        else:
            messages.error(request,"login failed")
            return redirect('signin')
    else:
        return render(request,'accounts/login.html')
def signout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'successful')
        return redirect('home')


def dashboard(request):
    user_id=request.user.id
    context=Contact.objects.order_by('contact_date').filter(user_id=user_id)


    return render(request,'accounts/dashboard.html',{"context":context})







# Create your views here.
