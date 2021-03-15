from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, BestSellerProducts, SaleProducts, Category
from django.shortcuts import get_object_or_404
from smtplib import SMTP
import json
import cowsay

# Create your views here.

class ProductListView(ListView):
    model= Product
    context_object_name='all_products'
    template_name='home/catalog.html'

def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    
    shopping_cart = json.loads(request.COOKIES.get('cart'))
    cowsay.milk(shopping_cart)

    return render(request, 'home/product-detail.html', {'product':product})


        
def filter_data(request):
    data_to_display = Product.objects.all()
    data = serializers.serialize('json', data_to_display)
    return HttpResponse(data)

def common_products(request):

    data = Product.objects.all()
    cowsay.milk(data)
    sale_products = SaleProducts.objects.all()
    best_seller = BestSellerProducts.objects.all()
    context = {
            'sale_products':sale_products,
            'best_seller':best_seller
        }

    return render(request, 'home/index.html', context)

""" SEARCH FUNCTIONALITY """
def search_product(request):
    if request:
        print('TRUE')
    else:
        print('NONE')
    
    search_query = request.GET.get('q')
    print(search_query)

    products = Product.objects.all().filter(
        Q(name__icontains=str(search_query))
    ).distinct()

    if products:
        return render(request, 'home/search-success.html', {'products': products})
    else:
        return redirect('mehsul_tapilmadi/')




""" CATEGORY LIST """

def category_product(request, id, slug):
    product = Product.objects.filter(category_id = id)
    return render(request, 'home/category.html', {'category_products':product})

"""  BUY ONE CLICK """

def buy_click(request, slug):
    if request.method == 'POST':
        product = Product.objects.get(slug=slug)
        username = request.POST.get('username')
        nomre = request.POST.get('phone_number')
        try:
            subject = f"Musterinin adi : {username} , Musterinin nomresi : {nomre} , Almaq istediyi mehsul {product.name}"
            message = "Yeni bir sifaris!!!"
            content = "Subject: {0}\n\n{1}".format(subject,message)

            myMailAdress = "osmanmammadov97@gmail.com"
            password = "20031997"

            sendTo = "osman.97.abi@gmail.com"

            mail = SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(myMailAdress,password)
            mail.sendmail(myMailAdress,sendTo,content.encode("utf-8"))
        except Exception as e:
            print("Error Handle\n {0}".format(e))

    return redirect('/')

    
