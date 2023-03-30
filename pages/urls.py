from pages import views
from django.urls import path

#from pages.views import Home
urlpatterns = [
   path('', views.home,name='home'),
   path('about/',views.about,name='about'),
    #path('',Home.as_view(),name='home'),
    #path('about/',About.as_view(),name='about')

]