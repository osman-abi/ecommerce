from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import AboutUs, Logistication, Guarantee, \
CreditTerms, PaymentTerms, EhomeAdress, Subscriber, Project,MostAsked

# Create your views here.

class About(ListView):
    model = AboutUs
    template_name='home/about-us.html'
    context_object_name = 'abouts'

class Logistica(ListView):
    model=Logistication
    template_name='home/service.html'
    context_object_name='services'

class Qaranti(ListView):
    model=Guarantee
    template_name='home/guarantee.html'
    context_object_name='guarantees'

class Credit(ListView):
    model=CreditTerms
    template_name = 'home/page-credit.html'
    context_object_name = 'credits'

class Payment(ListView):
    model = PaymentTerms
    template_name = 'home/payment-terms.html'
    context_object_name = 'payments'

class Adress(ListView):
    model = EhomeAdress
    template_name = 'home/location.html'
    context_object_name = 'adresses'

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        subs = Subscriber.objects.create(email=email)
        subs.save()
        return redirect('/')
    

class Projects(ListView):
    model = Project
    template_name = 'home/project.html'
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'home/project-detail.html'
    context_object_name = 'project'


class MostAskedQuestions(ListView):
    model = MostAsked
    template_name = 'home/most-asked-questions.html'
    context_object_name = 'questions'
