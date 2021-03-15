from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Campaign
# Create your views here.


class CampaignList(ListView):
    model = Campaign
    template_name = 'home/campaign.html'
    context_object_name = 'campaigns'

class CampaignDetail(DetailView):
    model = Campaign
    template_name = 'home/campaign-detail.html'
    context_object_name = 'campaign'