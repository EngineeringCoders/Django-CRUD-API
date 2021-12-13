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

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity':p_quantity,
        }

        cart_item = CartItem.objects.create(**product_data)
        data = {
        "message": "New item added to the cart"
        }
        return JsonResponse(data,status=201)

    #retrieving the data from the database using the GET request handler
    def get(self,request):
        #count() method counts the number of occurences in the databases
        item_counts = CartItem.objects.count()
        #all() method retrieves all the objects into a list of entities.
        items = CartItem.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'product_name':item.product_name,
                'product_price': item.product_price,
                'product_quantity':item.product_quantity
            })
        #creating the data in the form of python dictionary
        data = {
            'items': items_data,
            'count': item_counts,
        }
        #returning the data as a JSON response.
        return JsonResponse(data)


#updating a cart item by using the patch method
@method_decorator(csrf_exempt,name='dispatch')
class ShoppingCartUpdate(View):
    def patch(self,request, item_id):
        data = json.loads(request.body.decode('utf-8'))
        item = CartItem.objects.get(id=item_id)
        #changing the quantity of a product
        item.product_quantity = data['product_quantity']
        #using save() method to save the change in the database
        item.save()

        data = {
            'message': f'Item {item_id} has been updated'
        }

        return JsonResponse(data)

    #deleting the items from the cart
    def delete(self,request,item_id):
        item = CartItem.objects.get(id=item_id)
        #delete() method is used to delete the item on which it is called
        item.delete()

        data = {
            'message': f'Item {item_id} has been deleted'
        }
        return JsonResponse(data)
