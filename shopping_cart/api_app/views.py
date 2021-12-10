from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import json
from .models import CartItem
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create views for CartItem model
@method_decorator(csrf_exempt,name='dispatch')
class ShoppingCart(View):
    #definging a post method
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('product_name')
        p_price = data.get('product_price')
        p_quantity = data.get('product_quantity')
        print(p_name)
        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity':p_quantity,
        }
        print(product_data)

        cart_item = CartItem.objects.create(**product_data)
        data = {
        "message": f"New item added to the cart"
        }
        return JsonResponse(data,status=201)
