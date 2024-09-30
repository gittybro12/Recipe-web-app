from django.shortcuts import render,redirect
from .forms import UserRegisteration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = UserRegisteration
        if request.method == 'POST':
            form = UserRegisteration(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                messages.success(request, 'you have sucessfully created an account ' + user)
                form.save()
                return redirect('login')
            
    
    context = {'form':form}
    return render(request,'registration/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('Home')
            else:
                messages.info(request, 'Username or Password is incorrect')
  
    context= {}
    return render(request,'registration/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')