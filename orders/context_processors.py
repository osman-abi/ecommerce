from .models import Order
from products.models import Product
import json

def order(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order_model = Order.objects.get(customer=customer)
        items = order_model.orderitem_set.all()
        cart_items = order_model.get_cart_items #cart counting

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
                    'product':product,
                    'quantity': cart[i]['quantity']
                }

                items.append(item)
            except:
                print ('BLANK CART')
    return{
        'cart_items_count': cart_items,
        'items':items,
        'order':order_model
    }
