
from django.contrib import admin
from .models import Category, Product, PopularCategories, PostImage, BestSellerProducts, SaleProducts, Brend, Country, Color
from mptt.admin import DraggableMPTTAdmin



class CategoryAdmin(DraggableMPTTAdmin):

    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'artikul', 'price')
    search_fields = ('artikul',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(PopularCategories)
admin.site.register(PostImage)
admin.site.register(BestSellerProducts)
admin.site.register(SaleProducts)
admin.site.register(Brend)
admin.site.register(Country)
admin.site.register(Color)