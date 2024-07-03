from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]
    
    return render(request, 'contact/index.html', {'contacts': contacts, 'site_title': 'Contatos -'})



def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name} -'
    return render(request, 'contact/contact.html', {'contact': single_contact, 'site_title': site_title})



