# -*- encoding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session['user'] = user.id
                login(request, user)
                return redirect("/")
            else:
                msg = 'Dados de acesso incorretos' 
        else:
            msg = 'Formulário Invalido'    

    return render(request, "login.html", {"form": form, "msg" : msg})

