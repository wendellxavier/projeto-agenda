from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
        help_text='texto'
    )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
    )
    

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError('nome e sobre nome devem ser diferentes')
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()