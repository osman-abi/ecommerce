
from django.db import models
from ckeditor.fields import RichTextField



class Question(models.Model):
    title = models.CharField(max_length=500, blank=False, verbose_name='Sual Başlığı')
    answer = RichTextField(max_length=5000, blank=False, verbose_name='Cavab')


    class Meta:
        verbose_name = 'Tez-tez verilən sual'
        verbose_name_plural = 'Tez-tez verilən suallar'




    def __str__(self):
        return str(self.title)


