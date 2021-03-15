from .views import register_user,login_user

from django.urls import path

urlpatterns=[
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login_user')
]