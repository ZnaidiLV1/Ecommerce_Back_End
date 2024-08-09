from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('authentification.urls')),
    path('app1/',include('app1.urls'))
]
