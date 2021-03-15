
from django.db import models





class Resume(models.Model):
    first_name = models.CharField(max_length=150, blank=False, verbose_name='Ad')
    last_name = models.CharField(max_length=150, blank=False, verbose_name='Soyad')
    father_name = models.CharField(max_length=150, blank=False, verbose_name='Ata adi')
    phone_number = models.CharField(
        max_length=150, blank=False, verbose_name='telefon nomresi')
    age = models.CharField(max_length=150, blank=False, verbose_name='yasiniz')
    education = models.CharField(
        max_length=150, blank=False, verbose_name='tehsiliniz')
    city = models.CharField(max_length=150, blank=False,
                            verbose_name='sheher')
    job_practice = models.CharField(
        max_length=150, blank=False, verbose_name='Ish Tecrubeniz')
    vacation_name = models.CharField(
        max_length=150, blank=False, verbose_name='Muraciet etdiyiniz vakansiya')
    ability = models.CharField(
        max_length=150, blank=False, verbose_name='bacariqlariniz')



    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV-lər'



    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


# ?????
    class ActiveVacation(models.Model):
        pass

