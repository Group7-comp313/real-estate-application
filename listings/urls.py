from . import views
from django.urls import path
from .views import ListingsListView
from .views import ListingsDetailView

urlpatterns = [
    # path('/li',views.listing,name='list'),
    path('', ListingsListView.as_view(), name='listings'),
    path('<int:pk>/', ListingsDetailView.as_view(), name='listing'),
    path('search/<int:pk>/', ListingsDetailView.as_view(), name='listing'),
    path('search/',views.search,name='search')
    #path('',views.search,name='search')
]
