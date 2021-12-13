#application level url
from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate

urlpatterns = [
    path('cart-items/',ShoppingCart.as_view()),
    #adding URL-variable <int:item_id> - dynamic component of the url
    path('update-item/<int:item_id>',ShoppingCartUpdate.as_view()),
]
