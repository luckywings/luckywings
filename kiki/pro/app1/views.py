from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app1 .models import*
# Create your views here.

def base(request):
    d=student.objects.all()
    return render(request,'home.html',{'s':d})




def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already  exists!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')
                
      
    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(base)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(user_login)            
        