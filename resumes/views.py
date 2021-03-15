from django.shortcuts import render
from .models import Resume

# Create your views here.


def send_resume(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        education = request.POST.get('education')
        city = request.POST.get('city')
        job_practice = request.POST.get('job_practice')
        vacation_name = request.POST.get('vacation_name')
        ability = request.POST.get("ability")
        resume = Resume.objects.create(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            phone_number=phone_number,
            age=age,
            education=education,
            city=city,
            job_practice=job_practice,
            vacation_name=vacation_name,
            ability=ability
        )
        resume.save()
        return redirect ('/')

    
