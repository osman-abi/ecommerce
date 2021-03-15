import json
from .models import OrderItem, Order



def cookie_cart(request):
    try:
        shopping_cart = json.loads(request.COOKIES['cart'])
    except:
        shopping_cart = {}
        order = {'get_cart_items': 0}
        cart_items = order['get_cart_items']
        items = []
        for index in shopping_cart:
            cart_items += shopping_cart[index]["quantity"]
            product = Product.objects.get(id=index)
            total = (product.price * shopping_cart[index]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart_items

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name
                }
            }
            items.append(item)
			
    return {'cart_items' : cart_items , 'order' : order , 'items' : items}
