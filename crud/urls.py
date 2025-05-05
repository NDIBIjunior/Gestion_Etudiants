from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ajout/', views.ajout, name="ajout"),
    path('modifier-etudiant/<int:pk>/', views.update_etudiant, name='modifier-etudiant'),
    path('supprimer-etudiant/<int:pk>/', views.delete_etudiant, name='supprimer-etudiant'),
    path('profile/<int:pk>/', views.voir_profile, name='profile'),
]
