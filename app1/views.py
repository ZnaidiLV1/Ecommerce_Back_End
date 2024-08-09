from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
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



    # Create your views here.
