from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug= slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.category_name

class Quantity(models.Model):
    quantity_name=models.CharField(max_length=20)

    def __str__(self):
        return self.quantity_name

class Size(models.Model):
    size_name=models.CharField(max_length=20)

    def __str__(self):
        return self.size_name


class Product(models.Model):
    category = ForeignKey(Category, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    image= models.ImageField(upload_to='static/products', default="")
    price=models.CharField(max_length=20)
    description=models.TextField()
    stock=models.IntegerField(default=100)

    quantity=ForeignKey(Quantity, blank=True,null=True,on_delete=models.PROTECT)
    size=ForeignKey(Size, blank=True,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name
