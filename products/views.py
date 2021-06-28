from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProductView(APIView):
    def get(self,request):
        queryset= Product.objects.all()
        serializer = ProductSerializer(queryset, many = 'TRUE')
        return Response(serializer.data)


class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request.user)
        return Response({'sucess':"Hello Buddy"})
        
        
        