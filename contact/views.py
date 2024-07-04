from django.http import Http404
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]
    
    return render(request, 'contact/index.html', {'contacts': contacts, 'site_title': 'Contatos -'})



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
    
    return render(request, 'contact/index.html', {'contacts': contacts, 'site_title': 'Contatos -', 'search_value': search_value})

