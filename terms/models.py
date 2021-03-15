
from django.db import models
from ckeditor.fields import RichTextField





class Terms(models.Model):
    credit_terms = RichTextField(max_length=5000, blank=True, verbose_name='Kredit şərtləri')
    pay_terms = RichTextField(max_length=5000, blank=True, verbose_name='Ödəmə şərtləri')



    class Meta:
        verbose_name = 'Şərtlər'
        verbose_name_plural = 'Şərtlər'



    def __str__(self):
        return "Şərtlər"

