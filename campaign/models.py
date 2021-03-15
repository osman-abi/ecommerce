
from django.db import models
from ckeditor.fields import RichTextField





class Campaign(models.Model):
    title = models.CharField(max_length=500, blank=False, verbose_name='Başlıq')
    duration = models.CharField(max_length=250, blank=False, verbose_name='Zaman aralığı')
    small_text = RichTextField(max_length=300, blank=False, verbose_name='Qısa mətn')
    content = RichTextField(max_length=5000, blank=False, verbose_name='Ətraflı mətn')



    class Meta:
        verbose_name = 'Kampaniya'
        verbose_name_plural = 'Kampaniyalar'





    def __str__(self):
        str(self.title)


