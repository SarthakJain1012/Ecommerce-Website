from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price=models.FloatField(default=0)

    def __str__(self):
        return self.user.username
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(default=0)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product)

@receiver(pre_save,sender=CartItem)
def correct_price(sender,instance,*args,**kwargs):
    price_of_product=Product.objects.get(id=instance.product.id)
    instance.price=instance.quantity * float(price_of_product.price)
    print(instance.price)
    total_cart_items=CartItem.objects.filter(user = instance.user)

    cart = Cart.objects.get(id=instance.cart.id)
    cart.total_price +=instance.price
    cart.save()
    