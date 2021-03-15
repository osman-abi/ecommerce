from django.urls import path
from .views import SlideListView

urlpatterns[
    path('', SlideListView.as_view(), name='slides')
]