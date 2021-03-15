from .models import Favourite
from products.models import Product
import json

def favourite(request):
    try:
        favourite_product = json.loads(request.COOKIES['favourite'])
    except:
        favourite_product = {}

    favourite_items = []
    favourite_model = {'quantity':0}
    items_count = favourite_model['quantity']

    for i in favourite_product:
        try:
            product = Product.objects.get(slug=i)
            items_count += favourite_product[i]['quantity']

            item = {
                'product':product,
                'quantity':favourite_product[i]['quantity']
            }

            favourite_items.append(item)
        except:
            print('BLANK FAVOURITE')

    return {
        'favourite_items_count':items_count,
        'favourite_items':favourite_items
    }