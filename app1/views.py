from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import *
from.serializer import *

@api_view(['POST'])
def create_cat(request):
    try:
        data = request.data
        category = Category.objects.create(
            cat_name=data["cat_name"]
        )
        serializer = categorySerializer(category, many=False)
        return Response(serializer.data)
    except Exception as e:
        # Handle any other exception
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_cat(request):
    categories=Category.objects.all()
    serializer=categorySerializer(categories,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_item(request):
    try:
        data = request.data
        item_cat = Category.objects.get(cat_id=data["item_cat"])

        item = Item.objects.create(
            item_name=data["item_name"],
            item_desc=data["item_desc"],
            item_image=data["item_image"],
            item_count=int(data["item_count"]),
            item_active=bool(data["item_active"]),
            item_price=int(data["item_price"]),
            item_discount=int(data["item_discount"]),
            item_cat=item_cat  # Assign the foreign key relation
        )

        # Serialize the created item
        serializer = itemserializer(item, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    except ValidationError as e:
        return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_items(request,item_cat):
    items=Item.objects.filter(item_cat=item_cat)
    serializer=itemserializer(items,many=True)
    return Response(serializer.data)

    # Create your views here.
