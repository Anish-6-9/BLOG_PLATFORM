from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from . models import registration

# Create your views here.

import datetime


# @login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        posts = request.POST['post']

        print(title, posts)

    user = User.objects.all()

    return render(request, 'blog/home.html', {'user': user})


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            error = {'please enter same password.': ''}

            return render(request, 'blog/register.html', {'er': error})

        registration.objects.create(firstname=firstname, lastname=lastname, gender=gender,
                                    username=username, email=email, password=password)
        User.objects.create_user(
            username=username, email=email, password=password)

        return redirect('login')

    return render(request, 'blog/register.html')


def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username1, password=password1)

        if user:
            login(request, user)
            return redirect('home')
        else:
            logout(request)
            return redirect('login')

    return render(request, 'blog/login.html')


def logout(request):
    logout(request)
    return redirect('login')


def edit(request):
    return render(request, 'blog/home.html')
