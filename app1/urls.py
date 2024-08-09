from django.urls import path

from .views import *

urlpatterns =[
    path('create_cat/',create_cat),
    path('get_cat',get_cat)
    ]