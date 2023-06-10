from django.urls import path
from . import views

urlpatterns = [
    path('',views.hotel_index,name='hotel_index'),
]
