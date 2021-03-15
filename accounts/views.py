from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Customer

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            last_name=lastname,
            email=email,
            password=password
        )
        user.save()

        phone_number = request.POST.get('phone_number')
        customer = Customer.objects.create(
            user=user,
            phone_number=phone_number
        )
        customer.save()

        return redirect('/')
    return render(request, 'base.html',{'user':user})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect ('/')

    


