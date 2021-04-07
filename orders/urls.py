from django.urls import path
from .views import add_to_cart,checkout,update_cart,save_order

urlpatterns = [
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update_cart/', update_cart, name='update_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_save/', save_order, name='order_save')

]
