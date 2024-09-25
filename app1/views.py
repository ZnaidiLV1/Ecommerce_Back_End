from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import *
from .serializer import *


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
    categories = Category.objects.all()
    serializer = categorySerializer(categories, many=True)
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
            item_cat=item_cat
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
def get_items(request, item_cat):
    items = Item.objects.filter(item_cat=item_cat)
    serializer = itemserializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_favorite(request):
    data = request.data
    user = CustomUser.objects.get(email=data["email"])
    item = Item.objects.get(item_id=data["item_id"])
    fav = Favorite.objects.create(
        fav_user=user,
        fav_item=item
    )
    serializer = favserializer(fav, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_favorite(request, id):
    favorite_items = Favorite.objects.filter(fav_user=id).values_list('fav_item', flat=True)
    items = Item.objects.filter(item_id__in=favorite_items)
    serializer = itemserializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_items_bool(request, item_cat, id_user):
    items = Favorite.objects.filter(fav_user=id_user).values_list('fav_item', flat=True)
    items_cat_x = Item.objects.filter(item_id__in=items, item_cat=item_cat)
    all_items_cat_x=Item.objects.filter(item_cat=item_cat)
    list_bool = []
    for item in all_items_cat_x:
        if items_cat_x.filter(item_id=item.item_id).exists():
            list_bool.append(True)
        else:
            list_bool.append(False)

    return Response(list_bool)


@api_view(['DELETE'])
def delete_favorite(request):
    data = request.data
    item_fav = Favorite.objects.get(fav_item=data["fav_item"])
    item_fav.delete()
    return Response("Favorite deleted successfully")

@api_view(['GET'])
def get_all_items(request):
    items=Item.objects.values_list("item_name",flat=True)
    return Response(items)

@api_view(['GET'])
def get_item(request,item_name):
    try:
        item = Item.objects.get(item_name=item_name)
        serializer = itemserializer(item, many=False)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response("Item does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(['POST'])
def create_cart(request):
    data=request.data
    item=get_object_or_404(Item,item_id=data["cart_item"])
    user=get_object_or_404(CustomUser,id=data["cart_user"])
    cart=Cart.objects.create(
        cart_item=item,
        cart_user=user,
        cart_quantity=int(data["cart_quantity"]),
        cart_count=int(item.item_count)
    )
    serializer=cartserializer(cart,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update_cart_quantity(request):
    data=request.data
    cart=get_object_or_404(Cart,cart_id=data["cart_id"])
    cart.cart_quantity=data["cart_quantity"]
    cart.save()
    serializer=cartserializer(cart,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_cart(request):
    data=request.data
    cart=get_object_or_404(Cart,cart_id=data["cart_id"])
    cart.delete()
    return Response("Cart deleted successfully")

@api_view(['GET'])
def get_carts(request,cart_user):
    items_id_list=Cart.objects.filter(cart_user=cart_user).values_list("cart_item",flat=True)
    items=Item.objects.filter(item_id__in=items_id_list).order_by('item_id')
    serializer=itemserializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_cart_quantity_list(request,cart_user):
    cart_quantity_list = Cart.objects.filter(cart_user=cart_user).values_list("cart_quantity", flat=True).order_by('item_id')
    return Response(cart_quantity_list)

@api_view(['PUT'])
def cart_add_quantity(request):
    data=request.data
    cart=Cart.objects.get(cart_id=data["cart_id"])
    cart.cart_quantity=cart.cart_quantity+1
    cart.save()
    serializer=cartserializer(cart,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def cart_remove_quantity(request):
    data=request.data
    cart=Cart.objects.get(cart_id=data["cart_id"])
    cart.cart_quantity=cart.cart_quantity-1
    cart.save()
    serializer=cartserializer(cart,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def item_remove_quantity(request):
    #it has to be updated
    data = request.data
    item = Item.objects.get(item_id=data["item_id"])
    item.item_count = item.cart_quantity + 1
    item.save()
    serializer = itemserializer(item, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_carts(request,cart_user):
    carts=Cart.objects.filter(cart_user=cart_user).order_by("cart_item")
    serializer=cartserializer(carts,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def is_in_Cart(request,cart_item,cart_user):
    is_in_cart=Cart.objects.filter(cart_user=cart_user,cart_item=cart_item).exists()
    return Response(is_in_cart)

# Create your views here.
