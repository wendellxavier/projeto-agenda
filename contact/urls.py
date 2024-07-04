from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    
    
    
    path('search/', views.search, name='search'),
    path('', views.index, name="index"),
]
