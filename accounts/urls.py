from accounts import views
from django.urls import path

#from pages.views import Home
urlpatterns = [
   path('register', views.register,name='register'),
   path('signin/',views.loginpage,name='signin'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('signout/',views.signout,name='signout'),


]
