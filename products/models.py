""" MEHSULLARIN CATEGORIYALARI """
from django.db.models.signals import pre_save
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
import string
import random
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Kateqoriya adı AZ')
    # name_ru = models.CharField(max_length=150, blank=False, null=True, verbose_name='Kateqoriya adı RU')
    parent = TreeForeignKey('self', related_name="childeren", blank=True,
                            null=True, on_delete=models.CASCADE, verbose_name="Üst Kateqoriya")
    image = models.ImageField(
        upload_to='uploads/category/', blank=True, verbose_name='Şəkil')
    slug = models.SlugField(unique=True, max_length=300,
                            blank=True, editable=False)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1: i-1: -1])

    @property
    def imageurl(self):

        try:
            url = self.image.url

        except:
            url = ''

        return url

    def get_absolute_url(self):
        return reverse('category-details', args=[str(self.slug)])

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i').
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

        return super(Category, self).save(*args, **kwargs)


class PopularCategories(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, verbose_name='Kateqoriya')

    class Meta:
        verbose_name = 'Populyar kateqoriya'
        verbose_name_plural = 'Populyar kateqoriyalar'

    def __str__(self):
        return str(self.category.name)


class PostImage(models.Model):
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return str(self.id)


class Color(models.Model):
    color_name = models.CharField(max_length=100, verbose_name='reng')

    def __str__(self):
        return self.color_name

class Country(models.Model):
    production_country = models.CharField(max_length=100, verbose_name='olke adi')

    def __str__(self):
        return self.production_country


class Brend(models.Model):
    brend_name = models.CharField(max_length=100, verbose_name='marka adi')

    def __str__(self):
        return self.brend_name

class Product(models.Model):
    name = models.CharField(max_length=250, blank=False,
                            verbose_name='Məhsulun adı AZ')
    # name_ru = models.CharField(max_length=250, blank=False, null=True, verbose_name='Məhsulun adı RU')
    artikul = models.CharField(
        max_length=250, blank=True, verbose_name='Məhsulun artikulu')
    category = models.ForeignKey(
        Category, blank=False, on_delete=models.CASCADE,null=True, verbose_name='Məhsulun kateqoriyası')
    thumbnail = models.ImageField(
        upload_to='products/thumbnails/', blank=False, verbose_name='Məhsulun əsas şəkli')

    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    images = models.ManyToManyField(
        PostImage, blank=True, verbose_name='Məhsulun şəkilləri')
    colors = models.ManyToManyField(Color, verbose_name='mehsulun rengleri')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    features = RichTextField(max_length=5000, blank=True,
                             verbose_name='Məhsulun xüsusiyyətləri')
    delivery = RichTextField(max_length=5000, blank=True,
                             verbose_name='Çatdırılma və quraşdırılma')
    payment = RichTextField(max_length=5000, blank=True, verbose_name='Ödəniş')
    loan_terms = RichTextField(
        max_length=5000, blank=True, verbose_name='Kredit şərtləri')
    # about_ru = RichTextField(max_length=5000, blank=True, null=True, verbose_name='Məhsul haqqında ümumi məlumat RU')
    price = models.IntegerField(
        default=0, blank=True, verbose_name='Məhsulun oz qiyməti')
    sale = models.IntegerField(
        default=0, blank=True, verbose_name='endirim faizi')
    rest_price = models.IntegerField(
        default=0, blank=True, verbose_name='Mehsulun endirimli qiymeti')
    slug = models.SlugField(unique=True, max_length=300,
                            blank=True, editable=False)
    genislik = models.IntegerField()
    yukseklik = models.IntegerField()
    derinlik = models.IntegerField()
    publish_date = models.DateTimeField(
        auto_now=True, verbose_name='Əlavə edilmə tarixi')
    in_stock = models.BooleanField(verbose_name='Anbarda?', default=False)
    is_new = models.BooleanField(verbose_name='Yenidir?', default=False)
    like_votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i').
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

        return super(Product, self).save(*args, **kwargs)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=False,
                            verbose_name='Musterinin adı')
    email = models.EmailField(max_length=254)
    commentary = models.TextField()


class BestSellerProducts(models.Model):
    product = models.ForeignKey(
        Product, blank=False, on_delete=models.CASCADE, verbose_name='Məhsul')

    class Meta:
        verbose_name = 'Çox satılan'
        verbose_name_plural = 'Çox satılanlar'

    def __str__(self):
        return str(self.product.name)


class SaleProducts(models.Model):
    product = models.ForeignKey(
        Product, blank=False, on_delete=models.CASCADE, verbose_name='Məhsul')

    class Meta:
        verbose_name = 'Endirimdə olan məhsul'
        verbose_name_plural = 'Endirimdə olan məhsullar'

    def __str__(self):
        return str(self.product.name)


""" PRODUCT PRE SAVE """


@receiver(pre_save, sender=Product)
def generate_artikul(sender, instance, **kwargs):
    instance.artikul = ''.join(
        random.choice(string.digits) for _ in range(10))
    return instance.artikul


@receiver(pre_save, sender=Product)
def calculate(sender, instance, **kwargs):
    percent = (instance.price * instance.sale) / 100
    instance.rest_price = instance.price - percent
    return instance.rest_price
