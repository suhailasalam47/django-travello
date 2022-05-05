from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')    
    else:
        return render(request,"login.html")    


def register(request):

    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')   
            else:    
                user= User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("created")
            
        else:
            messages.info(request,'password not matching') 
            return redirect('/')  
        
    else:    
      return render(request,'register.html')