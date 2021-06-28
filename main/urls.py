from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('soap', views.soap,name='soap'),
    path('shampoo', views.shampoo,name='shampoo'),
    path('oil', views.oil,name='oil'),
    path('contact', views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('search',views.search,name='search')
]