from django.shortcuts import render


# Create your views here.
def voiture_index(request):
    return render(request,"voiture/voiture_index.html")


