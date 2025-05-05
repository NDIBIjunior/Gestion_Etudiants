from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    date_naissance = models.DateField()
    filière = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return self.nom
    