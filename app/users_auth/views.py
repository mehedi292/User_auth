from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_user') 
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is exist')
                return redirect(register)
            else:
                print(username, password, email, first_name, last_name)
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.is_staff=True
                user.save()
                print("Success")
                return redirect('login_user')
    else:
        print("this is not post method")
    return render(request, 'register.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')
    
@login_required(login_url='login_user') 
def logout_user(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login_user') 
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        retype_password = request.POST['retype_password']
        
        if new_password==retype_password:  
            if request.user.check_password(old_password):
                user = request.user
                user.set_password(new_password)
                user.save()
            else:
                print('Old password does not match')
        return redirect('change_password')
    return render(request, 'password_change.html')
    

