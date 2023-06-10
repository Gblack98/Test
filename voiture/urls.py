from django.urls import path
from . import views

urlpatterns = [
    path('',views.voiture_index,name='voiture_index'),
]
