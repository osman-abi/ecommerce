from django.db import models
from ckeditor.fields import RichTextField



class Partner(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name='Ad')
    logo = models.ImageField(upload_to='uploads/partners/', blank=False, verbose_name='Logo')
    text = RichTextField(max_length=5000, blank=True, verbose_name='Mətn')



    class Meta:
        verbose_name = 'Partnyor'
        verbose_name_plural = 'Partnyorlar'



    def __str__(self):
        return str(self.name)


class Banner(models.Model):
    left_cover = models.ImageField(upload_to='uploads/banners/', verbose_name='reklam baneri')
    right_cover = models.ImageField(
        upload_to='uploads/banners/', verbose_name='reklam baneri')
