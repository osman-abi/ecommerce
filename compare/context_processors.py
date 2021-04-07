# from .models import compare
from products.models import Product
import json


def compare(request):
    try:
        compare_product = json.loads(request.COOKIES['compare'])
    except:
        compare_product = {}

    compare_items = []
    compare_model = {'quantity': 0}
    items_count = compare_model['quantity']

    for i in compare_product:
        try:
            product = Product.objects.get(slug=i)
            items_count += compare_product[i]['quantity']

            item = {
                'product': product,
                'quantity': compare_product[i]['quantity']
            }

            compare_items.append(item)
        except:
            print('BLANK compare')

    return {
        'compare_items_count': items_count,
        'compare_items': compare_items
    }
