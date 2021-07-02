from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
# Create your views here


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user=request.user
        print(user)
        return Response('It is working aage ka kaam kar jaldi se')
    
    def post(self,request):
        user=request.user
        data = request.data
        cart,_= Cart.objects.get_or_create(user=user,ordered=False)
        product = Product.objects.get(id=data.get('product'))
        price=product.price
        quantity=data.get('quantity')
        cart_items = CartItem(cart=cart,user=user,product=product,price=price,quantity=quantity)
        cart_items.save()
        return Response("Items Added")
    def update():
        pass
    
    def delete():
        pass