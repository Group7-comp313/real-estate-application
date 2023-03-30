from django.shortcuts import render
from django.utils import timezone
from listings.models import Listings
from django.views.generic import ListView, DetailView
from listings.search import bedroom_choices,price_choice,state_choices

"""
def listings(request):
    listings=Listings.objects.all()
    context={'listings':listings}

    return render(request, 'listings/listings.html',context)
def listing(request):
    return render(request, 'listings/listing.html')
"""
def search(request):
    listings=Listings.objects.order_by('-list_date')
    #hetiing information from from by using request.GEt

    #keywords

    if 'keywords' in request.GET:
            print(request.GET)
            keywords =request.GET['keywords']
            if keywords:
                listings=listings.filter(discription__icontains=keywords)
    if 'state' in request.GET:
            state =request.GET['state']
            if state:
                listings=listings.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
            bedrooms =request.GET['bedrooms']
            if bedrooms:
                listings=listings.filter(bedrooms__iexact=bedrooms)
    if 'city' in request.GET:
            city =request.GET['city']
            if city:
                listings=listings.filter(city__iexact=city)
    if 'price' in request.GET:
            price =request.GET['price']
            print(type(price))
            if price:
                listings=listings.filter(price__lte=price)



    context = {"listings":listings,
               "state_choices": state_choices,
               "bedroom_choices": bedroom_choices,
               "price_choice": price_choice,
               "values":request.GET
               }
    return render(request,'listings/search.html',context)

class ListingsListView(ListView):
    # default object is model_list
    # default template is model_list.html
    paginate_by = 3

    model = Listings
    #to filter data but the default object for class  based view is same
    #queryset = Listings.objects.filter(price__gte=25000)

    template_name = 'listings/listings.html'
   # def get_context_data(self, **kwargs):
     #   object = super().get_context_data(**kwargs)
      #  return object


class ListingsDetailView(DetailView):
    model = Listings
    template_name = 'listings/listing.html'
    #def get_context_data(self, **kwargs):
       # object = super().get_context_data(**kwargs)
       # return object


