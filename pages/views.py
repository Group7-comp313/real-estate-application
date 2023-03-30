from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from listings.models import Listings
from realtors.models import Realtor
from listings.search import state_choices,bedroom_choices,price_choice
from django.contrib.auth.models import User

def home(request):
    listings=Listings.objects.all().order_by('-list_date')[:3]
    context={'listings':listings,
             "state_choices":state_choices,
             "bedroom_choices":bedroom_choices,
             "price_choice":price_choice
             }
    return render(request,'pages/home.html',context)
def about(request):
    realtors = Realtor.objects.all().order_by('hire_date')
    mvp = Realtor.objects.get(is_mvp=True)
    context = {'realtors':realtors,'mvp_realtor':mvp}
    return render(request, 'pages/about.html',context)

#class Home(ListView):
   # model=Listings
    #queryset = Listings.objects.order_by('-list_date')[:3]
    #template_name = 'pages/home.html'
#class About(ListView):
    #model = Realtor
    #queryset = Realtor.objects.order_by('hire_date')
    #mahesh = Realtor.objects.all().filter(is_mvp=True)

    #template_name = 'pages/about.html'
    #def get_queryset(self):
        #return Realtor.objects.filter(is_mvp=True)

# Create your views here.
