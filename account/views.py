from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
       # accounts=requests.get("http://127.0.0.1:8000/api/account/register").json()
        username=request.data['username']
        password=request.data['password']
        firstname=request.data['fname']
        lastname=request.data['lname']
        email=request.data['email']
        user = User(username=username,last_name=lastname,first_name=firstname,email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Registration Successful')
        refresh = RefreshToken.for_user(user)
        return redirect('login')
        return Response({"status" : "Successfully Registered",'refresh': str(refresh), 'user_id' : user.id,
        'access': str(refresh.access_token),})
        

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
            
        else:
            messages.error(request,"Failed")
            return redirect('login')
        

def LogoutView(request):
    logout(request)
    messages.success(request,"Logout Successful")
    return redirect('index')

