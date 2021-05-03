from django import forms
from .models import Dato

class formupost(forms.ModelForm):
    class Meta:
        model = Dato
        fields = ('categoria')