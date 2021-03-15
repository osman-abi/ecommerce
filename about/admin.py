from django.contrib import admin
from .models import (AboutUs, Logistication, Guarantee,
                     CreditTerms, PaymentTerms, EhomeAdress, Subscriber, Project, ProjectImages,
                     MostAsked)

admin.site.register(AboutUs)
admin.site.register(Logistication)
admin.site.register(Guarantee)
admin.site.register(CreditTerms)
admin.site.register(PaymentTerms)
admin.site.register(EhomeAdress)
admin.site.register(Subscriber)
admin.site.register(ProjectImages)
admin.site.register(Project)
admin.site.register(MostAsked)

# Register your models here.
