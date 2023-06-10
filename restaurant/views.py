from django.shortcuts import render

# Create your views here.
def restaurant_index(request):
    return render(request,"restaurant/restaurant_index.html")