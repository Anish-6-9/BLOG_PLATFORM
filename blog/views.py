from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from . models import registration, BlogPost

# Create your views here.

import datetime


def base(request):
    users = registration.objects.all()
    return render(request, 'blog/base.html', {'users': users})


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

        user = User.objects.first()

        registration.objects.create(firstname=firstname, lastname=lastname, gender=gender,
                                    username=username, email=email, password=password, created_by=user, created_at=datetime.datetime.now())
        User.objects.create_user(
            username=username, email=email, password=password)

        return redirect('log_in')

    return render(request, 'blog/register.html')


def log_in(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(request, username=username1, password=password1)

        if user:
            login(request, user)
            return redirect('home')
        else:
            logout(request)
            return redirect('log_in')

    return render(request, 'blog/log_in.html')


def log_out(request):
    logout(request)
    return redirect('log_in')


@login_required(login_url='/login')
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        posts = request.POST['post']
        username = request.user.username

        user = User.objects.first()

        BlogPost.objects.create(title=title, post=posts,
                                username=username, created_by=user, created_at=datetime.datetime.now())

        print(title, posts)

    data = BlogPost.objects.all().order_by('created_at')

    return render(request, 'blog/home.html', {'data': data})


def searchbar(request):
    # for search funtionality
    searched = request.GET.get('search')

    if searched:
        results = BlogPost.objects.filter(
            username__icontains=searched).order_by('created_at')
    else:
        results = BlogPost.objects.none()

    return render(request, 'blog/home.html', {'results': results, 'searched': searched})


def profile(request):
    username = request.user.username
    userid = registration.objects.all()
    user_profile = BlogPost.objects.filter(username=username).all()
    return render(request, 'blog/profile.html', {'user_profile': user_profile, 'userid': userid})


def edit(request, pk):
    profile = registration.objects.get(reference_id=pk)
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        registration.objects.filter(reference_id=pk).update(
            username=username1, password=password1)
        User.objects.filter(id=request.user.id).update(
            username=username1)
        return redirect('home')

    return render(request, 'blog/edit.html', {'edit_profile': profile, })
