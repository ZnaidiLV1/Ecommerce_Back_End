from rest_framework import serializers
from .models import *


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class favserializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

class cartserializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
