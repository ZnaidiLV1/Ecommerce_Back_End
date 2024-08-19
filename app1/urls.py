from django.urls import path

from .views import *

urlpatterns =[
    # Category's urls
    path('create_cat/',create_cat),
    path('get_cat/',get_cat),
    # Item's urls
    path('create_item/',create_item),
    path('<int:item_cat>-get_items/',get_items),
    # Favorite
    path('create_favorite/',create_favorite),
    path('<int:id>-get_favorites/',get_favorite),
    path('<int:item_cat>-<int:id_user>-get_cat_favorite/',get_items_bool),
    path('delete_favorite/',delete_favorite),
    # Cart
    path('create_cart/',create_cart),
    path('update_cart_quantity/',update_cart_quantity),
    path('<int:cart_user>-get_carts/',get_carts),
    path('<int:cart_user>-get_all_carts/',get_all_carts),
    path('delete_cart/',delete_cart),
    path('<int:cart_user>-get_quantity_list/',get_cart_quantity_list),
    path('cart_add_quantity/',cart_add_quantity),
    path('cart_remove_quantity/',cart_remove_quantity),
]