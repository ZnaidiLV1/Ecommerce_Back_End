from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from authentification.models import CustomUser

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True,auto_created=True)
    cat_name=models.CharField(unique=True)
    cat_date=models.DateField(auto_now=True)

class Item(models.Model):
    item_id=models.AutoField(primary_key=True,auto_created=True)
    item_name=models.CharField()
    item_desc=models.CharField()
    item_image=models.CharField()
    item_count=models.IntegerField()
    item_active=models.BooleanField()
    item_price=models.IntegerField()
    item_discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )

    item_date=models.DateField(auto_now=True)
    item_cat=models.ForeignKey(Category,on_delete=models.CASCADE)

class Favorite(models.Model):
    fav_id=models.AutoField(primary_key=True,)
    fav_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    fav_item=models.ForeignKey(Item,on_delete=models.CASCADE)

class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    cart_user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    cart_item=models.ForeignKey(Item,on_delete=models.CASCADE)
    cart_quantity=models.IntegerField()
# Create your models here.
