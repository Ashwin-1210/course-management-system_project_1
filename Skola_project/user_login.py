from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from Skola_app.EmailBackend import EmailBackend
from django.template import RequestContext


def REGISTER(req):
    if req.method == "POST":
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')

        # check email

        if User.objects.filter(email=email).exists():
            messages.warning(req, 'Email are Already Exists !')
            return redirect('register')

        # check username

        if User.objects.filter(username=username).exists():
            messages.warning(req, 'Username are Already Exists !')
            return redirect('register')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('home')
    return render(req, 'registration/register.html')


# def LOGIN(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = EmailBackend.authenticate(username=email, password=password)

        if User != None:
            login(req, User)
            return redirect('home')
        else:
            messages.error(req, 'Email and password Are Invalid !')
            return redirect('login')
