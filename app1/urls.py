from django.urls import path

from .views import *

urlpatterns =[
    # Category's urls
    path('create_cat/',create_cat),
    path('get_cat/',get_cat),
    # Item's urls
    path('create_item/',create_item),
    path('<int:item_cat>-get_items/',get_items),
    ]