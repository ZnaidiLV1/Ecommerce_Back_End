from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

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
# Create your models here.
