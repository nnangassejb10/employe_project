from django.shortcuts import render

from .models import Employe # POUR IMPORTER LE MODELE EMPLOYE SI Y AVAIT PLUSIEURS ON DEVAIT METTRE * à la place de EMPLOYE

# Create your views here.

def liste_employes(request):
    employes = Employe.objects.all()# renvoyer tout les employés dans notre liste
    return render(request, 'employe/list.html' , {'employes': employes})
