from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="shophome"),
    path('about/',views.about,name="shopabout"),
    path('contact/',views.contact,name="shopcontact"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout/',views.checkout,name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]