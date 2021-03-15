from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order, OrderItem
from products.models import Product
import json
from .utils import cookie_cart
import cowsay
# Create your views here.


# def product(request, pk):
# 	product = Product.objects.get(id=pk)

# 	if request.method == 'POST':
# 		product = Product.objects.get(id=pk)
# 		#Get user account information
# 		try:
# 			customer = request.user.customer
# 		except:
# 			device = request.COOKIES['device']
# 			customer = Customer.objects.get_or_create(device=device)

# 		order = Order.objects.get_or_create(
# 			customer=customer)
# 		orderItem = OrderItem.objects.get_or_create(
# 			order=order, product=product)
# 		orderItem.quantity = request.POST['quantity']
# 		orderItem.save()

# 		return redirect('cart')

# 	context = {'product': product}
# 	return render(request, 'store/product.html', context)







# def checkout(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order = Order.objects.get_or_create(customer=customer)
#         items = order.orderitem_set.all()
#     else:
#         cookieData = cookie_cart(request)
# 		cart_items = cookieData['cart_items']
# 		order = cookieData['order']
# 		items = cookieData['items']
#     context = {'items': items, 'order':order, 'cart_items':cart_items}
#     return render(request, 'home/checkout.html', context=context)

def add_to_cart(request):
	data = json.loads(request.body)

	productSlug = data['productSlug']
	action = data['action']	
	customer = request.user.customer
	product = Product.objects.get(slug=productSlug)
	
	order = Order.objects.get(customer=customer)
	order_item, created = OrderItem.objects.get_or_create(order=order, items=product)
	order_item.quantity += 1
	
	order_item.save()
	cowsay.milk(order_item.quantity)

	

	
	

	# if action == 'add':
	# 	order_item.quantity = (order_item.quantity + 1)

	# elif action == 'remove':
	# 	order_item.quantity = (order_item.quantity - 1)

	# order_item.save()

	# if order_item.quantity <= 0:
	# 	order_item.delete()

	return JsonResponse('item was added', safe=False)

""" CHECKOUT """
"""
def checkout(request):
	order_item = Order.orderitem_set.all()
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		phone = request.POST.get('phone')
		shipping_address = request.POST.get('shipping_address')
		order = Order.objects.create(customer=request.user.customer,
									first_name=first_name,
									last_name=last_name,
									phone=phone,
									shipping_address=shipping_address)
		order.save()
		return redirect('/')
	return render(request,'home/checkout.html',{'orders':order_item})
		
"""