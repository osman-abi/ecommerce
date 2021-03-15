from django.urls import path
from .views import PartnersList

urlpatterns = [
    path('', PartnersList.as_view(), name='partner')
]