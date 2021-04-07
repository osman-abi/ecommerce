from products.models import Product
from django.db import models
from ckeditor.fields import RichTextField
import random
import string


# customer


def transaction_id_generator(size=6, chars=string.digits):

    return ''.join(random.choice(chars) for _ in range(size))


def taksit_transaction_id_generator(size=5, chars=string.digits):

    return ''.join(random.choice(chars) for _ in range(size))

""" MUSTERININ SIFARISI """
""" Sifaris et' requesti getdiyi zaman checkout sehifesine atir,
    checkout sehifesinde asagida gosterilen forum doldururlur,
    tesdiq et requesti getdiyi zaman qebul edilmis sifarisler bolmesine dusur
 """
# :::::::::::::::::::::::::::::::::::::::::::::::::
class Order(models.Model):
    customer = models.ForeignKey(
        'accounts.Customer', on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Ad')
    last_name = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Soyad')
    phone = models.CharField(max_length=200, blank=True,
                             null=True, verbose_name='Telefon nömrəsi')
    taksit = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Taksit')
    shipping_address = models.TextField(
        max_length=5000, blank=True, null=True, verbose_name='Çatdırılacaq ünvan')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='Transaction id')
    taksit_transaction_id = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='Taksit Transaction id')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        # taksit

        if self.taksit_transaction_id is None or self.taksit_transaction_id == '':
            self.taksit_transaction_id = taksit_transaction_id_generator()

        unique_taksit_transaction_id = self.taksit_transaction_id

        while Order.objects.filter(taksit_transaction_id=unique_taksit_transaction_id).exists():
            unique_taksit_transaction_id = taksit_transaction_id_generator()

        self.taksit_transaction_id = unique_taksit_transaction_id

        return super(Order, self).save(*args, **kwargs)

    @property
    def get_cart_total(self):
        total = sum([item.get_total for item in self.orderitem_set.all()])
        return total

    @property
    def get_cart_items(self):
        total = sum([item.quantity for item in self.orderitem_set.all()])
        return total

""" Shopping Cart """
""" Sebetdeki mehsullari gosteren model """
# ::::::::::::::::::::::::::::::::::::::::::
class OrderItem(models.Model):
    items = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    


    def __str__(self):
        return self.items.name



    @property
    def get_total(self):
        total = self.items.price * self.quantity
        return total







""" QEBUL EDILMIS SIFARIS """
""" Checkout tesdiqlendikden sonra sifariw qebul olunur
    sifariw qebul olundugu zaman odenis sistemi de daxil olmaqla 
    qebul edilmis sifarisler formasinda databasa'ya oturur
 """    
# :::::::::::::::::::::::::::::::::::::::::::::
class ApprovedOrder(models.Model):

    STATUS = (
        ('approved', 'Qəbul edilib'),
        ('being_delivered', 'Çatdırılır'),
        ('recieved', 'Təhvil verilib'),
    )

    order_user = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, verbose_name='İstifadəçi')
    firstname = models.CharField(max_length=150, blank=False, verbose_name='Ad')
    lastname = models.CharField(max_length=150, blank=False, verbose_name='Soyad')
    phone = models.CharField(max_length=30, blank=False, verbose_name='Əlaqə nömrəsi')
    taksit = models.CharField(max_length=30, blank=True, null=True, verbose_name='Taksit')
    items = models.ManyToManyField('OrderItem', blank=True, verbose_name='Məhsullar')
    ordered_date = models.DateTimeField(auto_now=True,verbose_name='Sifarişin edilmə tarixi')
    shipping_address = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Çatdırılacaq ünvan')
    amount = models.CharField(max_length=100, blank=True, null=True, verbose_name='Məbləğ')
    status = models.CharField(choices=STATUS, default='approved', max_length=40, blank=True)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    taksit_transaction_id = models.CharField(max_length=500, blank=True, null=True, verbose_name='Taksit Transaction id')



    class Meta:
        verbose_name = 'Təsdiqlənmiş Sifariş'
        verbose_name_plural = 'Təsdiqlənmiş Sifarişlər'




    def __str__(self):
        return str(self.firstname) + " " + str(self.lastname)


