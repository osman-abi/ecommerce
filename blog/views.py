from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.

class BlogList(ListView):
    model = Article
    template_name = 'home/blog.html'
    context_object_name = 'blogs'

class BlogDetail(DetailView):
    model = Article
    template_name = 'home/blog-detail.html'
    context_object_name = 'blog'
    


