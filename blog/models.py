
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify







class Article(models.Model):
    image = models.ImageField(upload_to='uploads/blog/', blank=False, verbose_name='Şəkil')
    title = models.CharField(max_length=300, blank=False, verbose_name='Başlıq')
    content = RichTextField(max_length=5000, blank=True, verbose_name='Mətn')



    class Meta:
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'


    @property
    def imageurl(self):

        try:
            url = self.image.url

        except:
            url = ''

        return url



    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('article-details', args=[str(self.slug)])


    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i').
                       replace('ə', 'e').
                       replace('ö', 'o').
                       replace('ğ', 'g').
                       replace('ç', 'c').
                       replace('ş', 's').
                       replace('ü', 'u').
                       replace('ı', 'i').
                       replace('Ə', 'e').
                       replace('Ö', 'o').
                       replace('Ğ', 'g').
                       replace('Ç', 'c').
                       replace('Ş', 's').
                       replace('Ü', 'u').
                       replace('I', 'i'))

        return slug


    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Article, self).save(*args, **kwargs)

