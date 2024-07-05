from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)
        widgets = {'first_name': forms.TextInput(attrs= {'placeholder': 'digite seu nome'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'digite seu sobrenome'}),
                   'phone': forms.TextInput(attrs={'placeholder': 'digite número do seu telefone'})}
        
    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError('erro'))
        return super().clean()