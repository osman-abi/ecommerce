from django.shortcuts import render
from django.generic.views import ListView
from .models import Slide


# Create your views here.

class SlideListView(ListView):
    model=Slide
    context_object_name='slides'
    template_name='base.html'
    