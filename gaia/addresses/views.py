from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address

class AddressView(CreateView):
    model = Address
    fields = ['address']
    template_name = 'addresses/home.html'
    success_url = '/'