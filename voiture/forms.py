from django import forms
from .models import Vehicule

class NewCarForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['marque', 'modele', 'prix_par_jour', 'id_admin', 'photo']
