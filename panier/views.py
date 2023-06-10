from django.shortcuts import render

# Create your views here.
def panier_index(request):
    return render(request,"panier/panier_index.html")