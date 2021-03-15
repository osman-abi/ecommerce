from django.urls import path
from .views import (
    About,
    Logistica,
    Qaranti,
    Credit,
    Payment,
    Adress,
    subscribe,
    Projects,
    ProjectDetail,
    MostAskedQuestions
)

urlpatterns=[
    path('', About.as_view(),name='about'),
    path('unvan/', Adress.as_view(), name='location'),
    path('catdirilma_ve_qurasdirilma/', Logistica.as_view(), name='logistica'),
    path('zemanet/', Qaranti.as_view(), name='zemanet'),
    path('kredit/', Credit.as_view(),name='page_credit'),
    path('payment/', Payment.as_view(), name='payment_terms'),
    path('subscribe/', subscribe, name='subscribe'),
    path('layiheler/', Projects.as_view(), name='projects'),
    path('layihe/<int:pk>', Payment.as_view(), name='project_detail'),
    path('suallar/', MostAskedQuestions.as_view(), name='questions'),
]
