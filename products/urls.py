from django.urls import path
from django.views.generic import TemplateView
from .views import (
    common_products,
    product_detail,
    ProductListView,
    search_product,
    buy_click,
    filter_data,
    category_product
)

urlpatterns = [
    path('', common_products, name='home'),
    path('get_data/',filter_data),

    path('search/', search_product, name='search_success'),
    path('search/mehsul_tapilmadi/',
         TemplateView.as_view(template_name='home/search-error.html')),
    path('category_detail/<int:id>/<slug:slug>', category_product, name='category_detail'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<slug>/', product_detail, name='product_detail'),
    path('buy_click/<slug:slug>', buy_click, name='buy_click'),
]
