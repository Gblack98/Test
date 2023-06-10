from django.urls import path
from . import views

urlpatterns = [
    path('',views.panier_index,name='panier_index'),
]
