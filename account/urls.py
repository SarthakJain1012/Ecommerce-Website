from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login',views.LoginView,name='Loginview'),
    path('changepassword',views.ChangePasswordView,name='ChangePasswordView'),
    path('logout',views.LogoutView,name='LogoutView'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]