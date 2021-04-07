from .models import Order
from products.models import Product
import json

def order(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order_model = Order.objects.get(customer=customer)
        items = order_model.orderitem_set.all()
        cart_items = order_model.get_cart_items
        cart_total = order_model.get_cart_total #cart counting

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        items = []
        order_model = {'get_cart_items':0,'get_cart-total':0}
        cart_items = order_model['get_cart_items'] #cart counting
        cart_total = order_model['get_cart-total']

        for i in cart:
            try:
                product = Product.objects.get(slug=i)
                total = (product.price * cart[i]['quantity'])
                cart_total += total
                cart_items += cart[i]['quantity']

                item = {
                    'items':product,
                    'quantity': cart[i]['quantity'],
                    'common_total': cart_total,
                    'get_total':total
                }

                items.append(item)
            except:
                print ('BLANK CART')
    return{
        'cart_items_count': cart_items,
        'products':items,
        'order': order_model,
        'cart_total':cart_total
    }
