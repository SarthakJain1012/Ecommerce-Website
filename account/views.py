from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from django.contrib.auth import update_session_auth_hash
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
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        else:
            user = User(username=username,last_name=lastname,first_name=firstname,email=email)
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration Successful')
            refresh = RefreshToken.for_user(user)
            return redirect('login')
        #return Response({"status" : "Successfully Registered",'refresh': str(refresh), 'user_id' : user.id,
        #'access': str(refresh.access_token),})
        

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

def ChangePasswordView(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        old_password = request.POST['old_password']
        print(new_password1)
        current_user=request.user
        if new_password1 == new_password2:
            if current_user.username == username and current_user.email == email:
                user = authenticate(request, username=username, password=old_password)
                if user is not None:
                    current_user = User.objects.get(username=username)
                    current_user.set_password(new_password1)
                    current_user.save()
                    messages.success(request,"Password Reset Successful")
                    return redirect('index')
                else:
                    messages.error(request,"Old Password Wrong")
                    return redirect('changepassword')
            else:
                messages.error(request,"User does not exist")
                return redirect('changepassword')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('changepassword')


