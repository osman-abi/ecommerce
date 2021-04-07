from .models import Category
def category(request):
    return {'category': Category.objects.all(),
            # 'sale_products':SaleProducts.product_set.all()
        }