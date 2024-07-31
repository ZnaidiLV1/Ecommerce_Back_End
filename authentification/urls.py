from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns =[
    # login & logout
    path('login/', MyTokenObtainPairView.as_view(), ),
    path('token/refresh/', TokenRefreshView.as_view(),),
    path('logout/',logout),
    # Verification Code
    path('sendCode/',sendVerificationCode),
    path('verifyCode/',verifyVerificationCode),
    # Create User
    path('createUser/',create_user),

]