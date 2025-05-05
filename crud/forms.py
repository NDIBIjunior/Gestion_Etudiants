from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style commun pour tous les champs
        base_style = "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200"
        
        self.fields['nom'].widget.attrs.update({'class': base_style})
        self.fields['prenom'].widget.attrs.update({'class': base_style})
        self.fields['email'].widget.attrs.update({'class': base_style})
        self.fields['date_naissance'].widget.attrs.update({'class': base_style + ' datepicker', 'type': 'date'})
        self.fields['filière'].widget.attrs.update({'class': base_style})
        self.fields['photo'].widget.attrs.update({'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'})

    class Meta:
        model = Etudiant
        fields = '__all__'