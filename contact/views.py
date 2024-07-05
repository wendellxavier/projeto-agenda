from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)
        
    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError('erro'))
        return super().clean()

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'contact/index.html', {'page_obj': page_obj, 'site_title': 'Contatos -'})



def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name} -'
    return render(request, 'contact/contact.html', {'contact': single_contact, 'site_title': site_title})


def search(request):
    search_value = request.GET.get('q', '').strip()
    
    
    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) |
                                                        Q(phone__icontains=search_value) | Q(email__icontains=search_value)).order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    return render(request, 'contact/index.html', {'page_obj': page_obj, 'site_title': 'Contatos -', 'search_value': search_value})



def create(request):
    if request.method == 'POST':
        context = { 'form': ContactForm(request.POST)}
        
        return render(request, 'contact/create.html', context)   
    
    context = {'form': ContactForm()}
    
    return render(request, 'contact/create.html', context)
   
    