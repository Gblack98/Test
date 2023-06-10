from django.shortcuts import render

# Create your views here.
def hotel_index(request):
    return render(request,"hotel/hotel_index.html")