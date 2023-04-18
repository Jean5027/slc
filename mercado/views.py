from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import request
from django.contrib.auth import authenticate, login, logout
from . import models


def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    listas = models.Lista.objects.all()

    return render(request, "mercado/mercado.html", {
        'listas': listas,
    })



def logout_view(request):
    logout(request)
    return render(request, "mercado/login.html", {
                "message": "Logged Out"
            })



def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "mercado/login.html", {
                "message": "Invalid Credentials"
            })
        
    return render(request, "mercado/login.html")


def cadastrar_lista(request):
    if request.method == "POST":
        nome = request.POST.get('lista')
        lista = models.Lista.objects.create(nome=nome)
        lista.save()
        return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse('index'))


def apaga_lista(request): # Ajeitar aqui
    if request.method == "POST":
        nome = int(request.POST.get('lista'))
        lista = models.Lista.objects.get(id=nome)
        lista.delete()

        return HttpResponseRedirect(reverse('index'))
    
    return HttpResponseRedirect(reverse('index'))
