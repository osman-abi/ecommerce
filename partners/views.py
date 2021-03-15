from django.shortcuts import render
from django.views.generic import ListView
from .models import Partner

# Create your views here.

class PartnersList(ListView):
    model = Partner
    template_name = 'home/partner.html'
    context_object_name = 'partners'
