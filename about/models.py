from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=100, default='Haqqimizda')
    content = RichTextField(verbose_name='Haqqimizda Melumat')

    def __str__(self):
        return self.title

class Logistication(models.Model):
    title = models.CharField(
        max_length=100, default='Çatdırılma və quraşdırılma')
    content = RichTextField(verbose_name='Çatdırılma haqqinda Melumat')

    def __str__(self):
        return self.title


class Guarantee(models.Model):
    title = models.CharField(
        max_length=100, default='Ehome zəmanəti')
    content = RichTextField(verbose_name='Zemanet haqqinda Melumat')

    def __str__(self):
        return self.title


class CreditTerms(models.Model):
    title = models.CharField(
        max_length=100, default='Kredit şərtləri')
    content = RichTextField(verbose_name='Zemanet haqqinda Melumat')

    def __str__(self):
        return self.title


class PaymentTerms(models.Model):
    title = models.CharField(
        max_length=100, default='Ödəmə şərtləri')
    content = RichTextField(verbose_name='Ödəmə şərtləri haqqinda Melumat')

    def __str__(self):
        return self.title


class EhomeAdress(models.Model):
    branch_name = models.CharField(max_length=300, verbose_name='Filialin adi')
    address = models.CharField(max_length=300, verbose_name='unvan')
    email = models.EmailField(verbose_name='Ehome mail unvani')
    phone_number = models.CharField(max_length=50, verbose_name='telefon nomresi')


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='abonentin email unvani')

    class Meta:
        verbose_name_plural='Abune olunmus istifadeciler'

    def __str__(self):
        return self.email

class ProjectImages(models.Model):
    image = models.ImageField(upload_to='uploads/projects/')

class Project(models.Model):
    title = models.CharField(
        max_length=100, default='Layihe şərtləri')
    content = RichTextField(verbose_name='Layiheler haqqinda Melumat')
    main_image = models.ImageField(upload_to='uploads/projects')
    image = models.ManyToManyField(ProjectImages)



class MostAsked(models.Model):
    title = models.CharField(
        max_length=300, verbose_name='sual')
    content = RichTextField(verbose_name='cavab')

    def __str__(self):
        return self.title
