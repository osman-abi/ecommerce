
from django.db import models




class Slide(models.Model):
    image = models.ImageField(upload_to='slide/uploads/', blank=False, verbose_name='Şəkil')



    class Meta:
        verbose_name = 'Slayd'
        verbose_name_plural = 'Slaydlar'



    def __str__(self):
        return str(self.image)
