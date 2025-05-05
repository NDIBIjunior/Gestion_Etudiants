from django.shortcuts import render, redirect, get_object_or_404
from .forms import EtudiantForm
from .models import Etudiant
from django.contrib import messages
# Create your views here.

def index(request):
    etudiants = Etudiant.objects.all().order_by('filière')
    return render(request, 'index.html', {'etudiants':etudiants})


def ajout(request):
    if request.method == 'POST':
        print("FILES reçus :", request.FILES)
        form = EtudiantForm(request.POST, request.FILES)  # Gère les fichiers (photo)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('index')  # Redirige vers la liste après succès
    else:
        form = EtudiantForm()
    return render(request, 'ajout.html', {'form': form})


def update_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, id=pk)
    
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('index')  # Rediriger vers la liste des étudiants
    else:
        form = EtudiantForm(instance=etudiant)
    
    return render(request, 'modifier.html', {'form': form, 'etudiant': etudiant})


def delete_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, id=pk)
    if request.method == 'POST':
        etudiant.delete()
        messages.success(request, "L'étudiant a été supprimé avec succès.")
        return redirect('index')
    return redirect('index')

def voir_profile(request, pk):
    # Récupérer l'étudiant par son ID
    etudiant  = get_object_or_404(Etudiant, id=pk)
    
    return render(request, 'profile.html', {'etudiant': etudiant})
